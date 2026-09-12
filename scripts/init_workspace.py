#!/usr/bin/env python3
import argparse,json
from pathlib import Path

def initialize(root):
    root=Path(root).resolve();root.mkdir(parents=True,exist_ok=True)
    for name in ['source','samples','projects','output']: (root/name).mkdir(exist_ok=True)
    state=root/'workspace.json'
    if not state.exists(): state.write_text(json.dumps({'schemaVersion':1,'skill':'muddaser-video-editing-skills','projects':[]},indent=2)+'\n')
    return root
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('workspace');a=p.parse_args();print(initialize(a.workspace))
