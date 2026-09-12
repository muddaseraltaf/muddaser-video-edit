#!/usr/bin/env python3
import json,shutil,sys,subprocess
from pathlib import Path
root=Path(__file__).resolve().parents[1]
checks={'python_3_9_plus':sys.version_info>=(3,9),'ffmpeg':shutil.which('ffmpeg'),'ffprobe':shutil.which('ffprobe'),'node':shutil.which('node'),'npm':shutil.which('npm'),'hyperframes':str(root/'node_modules/.bin/hyperframes') if (root/'node_modules/.bin/hyperframes').exists() else shutil.which('hyperframes'),'whisper_cli_optional':shutil.which('whisper-cli')}
if checks['node']:
    try:checks['node_22_plus']=int(subprocess.check_output([checks['node'],'--version'],text=True).strip().lstrip('v').split('.')[0])>=22
    except (ValueError,subprocess.SubprocessError):checks['node_22_plus']=False
else:checks['node_22_plus']=False
print(json.dumps({'checks':checks,'note':'Availability only; render, model and ASR smoke checks remain necessary.'},indent=2))
sys.exit(0 if all(checks[k] for k in ['python_3_9_plus','ffmpeg','ffprobe','node','node_22_plus','npm','hyperframes']) else 1)
