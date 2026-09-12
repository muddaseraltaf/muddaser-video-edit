import json,subprocess,sys,tempfile,unittest,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'scripts'))
from transcribe import normalize
from init_workspace import initialize

class PortableTests(unittest.TestCase):
    def test_invalid_timestamps(self):
        for s,e in [(math.nan,1),(0,math.inf),(-1,0),(1,.5),(0,3)]:
            with self.assertRaises(ValueError):normalize([{'text':'word','start':s,'end':e}],2)
    def test_workspace_preserves_existing(self):
        with tempfile.TemporaryDirectory() as t:
            p=initialize(t);f=p/'workspace.json';f.write_text('{"custom":true}');initialize(t);self.assertEqual(json.loads(f.read_text()),{'custom':True})
    def test_intake_and_import_cache(self):
        with tempfile.TemporaryDirectory() as t:
            p=Path(t);media=p/'source with spaces.mp4'
            subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','color=c=blue:s=240x320:d=2:r=30','-f','lavfi','-i','sine=frequency=440:duration=2','-c:v','libx264','-pix_fmt','yuv420p','-c:a','aac','-shortest',str(media)],check=True)
            project=p/'project';subprocess.run([sys.executable,str(ROOT/'scripts/intake.py'),str(media),'--project',str(project)],capture_output=True,check=True)
            self.assertTrue((project/'review/contact.jpg').exists())
            words=p/'import.json';words.write_text(json.dumps([{'text':'سلام','start':.1,'end':.8}],ensure_ascii=False))
            cmd=[sys.executable,str(ROOT/'scripts/transcribe.py'),str(media),'--project',str(project),'--language','ur','--import-json',str(words)]
            subprocess.run(cmd,capture_output=True,check=True);before=(project/'transcript.json').read_bytes()
            r=subprocess.run(cmd,capture_output=True,text=True,check=True);self.assertTrue(json.loads(r.stdout)['reused']);self.assertEqual(before,(project/'transcript.json').read_bytes())
            words.write_text(json.dumps([{'text':'changed','start':.1,'end':.8}]));r=subprocess.run(cmd,capture_output=True);self.assertNotEqual(r.returncode,0);self.assertEqual(before,(project/'transcript.json').read_bytes())
if __name__=='__main__':unittest.main()
