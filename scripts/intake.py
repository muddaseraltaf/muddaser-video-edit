#!/usr/bin/env python3
import argparse, hashlib, json, subprocess, os
from pathlib import Path

def run(args):
    return subprocess.run(args, check=True, capture_output=True, text=True).stdout

def digest(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for b in iter(lambda:f.read(8*1024*1024),b''): h.update(b)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser(); p.add_argument('source',type=Path);p.add_argument('--project',type=Path,required=True)
    a=p.parse_args();src=a.source.resolve(strict=True);dest=a.project.resolve();dest.mkdir(parents=True,exist_ok=True)
    identity=digest(src); out=dest/'intake.json'
    if out.exists() and json.loads(out.read_text())['sha256']!=identity:raise SystemExit('Project belongs to a different source; choose another directory.')
    meta=json.loads(run(['ffprobe','-v','error','-show_format','-show_streams','-of','json',str(src)]))
    duration=float(meta['format']['duration']); video=next((s for s in meta['streams'] if s['codec_type']=='video'),None)
    times=[round(duration*(i+.5)/6,3) for i in range(6)]
    images=dest/'review';images.mkdir(exist_ok=True)
    if video:
        for i,t in enumerate(times):
            run(['ffmpeg','-hide_banner','-loglevel','error','-y','-ss',str(t),'-i',str(src),'-frames:v','1','-vf','scale=320:480:force_original_aspect_ratio=decrease,pad=320:480:(ow-iw)/2:(oh-ih)/2:color=black',str(images/f'frame-{i:02d}.jpg')])
        run(['ffmpeg','-hide_banner','-loglevel','error','-y','-framerate','1','-i',str(images/'frame-%02d.jpg'),'-vf','tile=3x2','-frames:v','1',str(images/'contact.jpg')])
    siblings=[{'path':os.path.relpath(x.resolve(),dest),'bytes':x.stat().st_size} for x in src.parent.iterdir() if x.is_file() and x!=src and x.suffix.lower() in {'.png','.jpg','.jpeg','.webp','.mp4','.mov','.mkv','.wav','.mp3','.pdf'}]
    record={'source':os.path.relpath(src,dest),'sha256':identity,'duration':duration,'video':video,'audio':[s for s in meta['streams'] if s['codec_type']=='audio'],'sampleTimes':times,'contactSheet':str(Path('review')/'contact.jpg') if video else None,'companionCandidates':siblings,'analysisStatus':'Awaiting agent visual and transcript analysis; metadata is not a style classifier.'}
    out.write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n');print(out)
if __name__=='__main__':main()
