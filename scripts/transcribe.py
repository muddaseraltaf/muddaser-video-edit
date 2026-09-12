#!/usr/bin/env python3
"""Explicit-language local Hyperframes adapter or portable timestamp import."""
import argparse,json,math,os,subprocess
from pathlib import Path
from intake import digest,run

def normalize(raw,duration):
    words=raw if isinstance(raw,list) else raw.get('words',[])
    if not words:raise ValueError('No timestamped words supplied')
    result=[];last=-1
    for w in words:
        text=str(w.get('text',w.get('word',''))).strip()
        if not text:continue
        start,end=float(w['start']),float(w['end'])
        if not all(map(math.isfinite,[start,end])) or not 0<=start<=end<=duration+.05 or start<last:
            raise ValueError('Non-finite, out-of-range or unordered timestamp')
        result.append({'text':text,'type':'word','start':start,'end':end,'sourceStart':start,'sourceEnd':end});last=start
    if not result:raise ValueError('Transcript has no nonempty words')
    return {'text':' '.join(w['text'] for w in result),'audio_duration_secs':duration,'words':result}

def main():
    p=argparse.ArgumentParser();p.add_argument('source',type=Path);p.add_argument('--project',type=Path,required=True);p.add_argument('--language',choices=['en','ur'],required=True);p.add_argument('--import-json',type=Path);p.add_argument('--hyperframes',default='hyperframes');a=p.parse_args()
    src=a.source.resolve(strict=True);dest=a.project.resolve();dest.mkdir(parents=True,exist_ok=True)
    model='small.en' if a.language=='en' else 'large-v3';provider='import' if a.import_json else 'local-whisper'
    request={'sourceSha256':digest(src),'language':a.language,'provider':provider,'model':None if a.import_json else model,'importSha256':digest(a.import_json) if a.import_json else None,'adapterVersion':1}
    if not a.import_json:request['backendVersion']=run([a.hyperframes,'--version']).strip()
    state=dest/'transcription-state.json';output=dest/'transcript.json'
    if state.exists() or output.exists():
        if state.exists() and output.exists() and json.loads(state.read_text()).get('request')==request:
            print(json.dumps({'reused':True,'output':str(output)}));return
        raise SystemExit('Existing transcript has different input/settings or incomplete state; use a new project.')
    duration=float(json.loads(run(['ffprobe','-v','error','-show_entries','format=duration','-of','json',str(src)]))['format']['duration'])
    if a.import_json:raw=json.loads(a.import_json.read_text())
    else:
        model_file=Path.home()/'.cache/hyperframes/whisper/models'/f'ggml-{model}.bin'
        if not model_file.is_file():raise SystemExit(f'Missing model {model}; configure the Hyperframes model cache or import a transcript. No automatic model download.')
        args=[a.hyperframes,'transcribe',str(src),'--dir',str(dest/'raw-asr'),'--engine','whisper','--model',model,'--language',a.language,'--json']
        proc=subprocess.run(args,env={**os.environ,'HYPERFRAMES_NO_TELEMETRY':'1'},capture_output=True,text=True)
        if proc.returncode:raise SystemExit(proc.stderr+'\n'+proc.stdout)
        raw=json.loads((dest/'raw-asr/transcript.json').read_text())
    t=normalize(raw,duration)
    output.write_text(json.dumps(t,ensure_ascii=False,indent=2)+'\n');(dest/'words.json').write_text(json.dumps(t['words'],ensure_ascii=False,indent=2)+'\n');(dest/'transcript.txt').write_text(t['text']+'\n')
    state.write_text(json.dumps({'request':request,'sourceRelativeToProject':os.path.relpath(src,dest),'reviewRequired':True},indent=2)+'\n')
    print(json.dumps({'ok':True,'words':len(t['words']),'output':str(output)}))
if __name__=='__main__':main()
