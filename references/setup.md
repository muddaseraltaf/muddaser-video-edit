# Setup on another host

The package is portable guidance plus helpers. It does not contain the original footage, sample videos, model weights, third-party skill installations or a ready-made transcript for a new source.

## Required tools
- Python 3.9+ for helpers (standard library only).
- FFmpeg and FFprobe on PATH for intake and verification. Install through a trusted platform package manager; check needed HDR filters before conversion.
- Node 22+ / npm and the dependencies in package.json for the established Hyperframes/GSAP renderer. `npm install` in this repository; `python3 scripts/doctor.py` reports availability.
- Local Whisper support/models only if transcribing here. Hyperframes' transcribe engine is the established adapter; inspect `./node_modules/.bin/hyperframes transcribe --help` and its current model setup. Models are separate large downloads, not silently installed by our helpers. An imported timestamped transcript needs no ASR model.

Hyperframes 0.8.35 and GSAP 3.14.2 are the last established baseline for these helpers. This is not a claim they are the latest. Follow official version-specific documentation for upgrades, then verify a small composition and keep a lockfile. `doctor.py` reports the environment; a successful check doesn't prove rendering or ASR works. Python helper tests require FFmpeg/FFprobe.

Create a workspace with `python3 scripts/init_workspace.py /path/to/workspace`. The script creates missing folders and state without overwriting existing data. Install the skill separately or keep it beside the workspace; use explicit script paths when outside the repository.

## Renderer contract
When official Hyperframes domain skills are available, use their current version-matched contracts for exact syntax. This package supplies creative direction and small motion helpers, not a frozen copy of all upstream docs. Start with `hyperframes --help`, `check --help` and `render --help` from the local executable. Core reference: https://github.com/heygen-com/hyperframes.

Established composition pattern: fixed-size root with composition ID/dimensions/duration, timed media with stable IDs and start/duration/track attributes, muted visual video and separate narration audio, one paused GSAP timeline registered under the composition ID. Renderer controls media playback; do not add independent animation clocks or a competing requestAnimationFrame loop.

Local browsers or GPU ASR may need execution permissions on the new host. Explain actual failures and use that host's permission flow; instructions cannot override it. Browse/capture/generate only through available authorized tools, and keep the same honest evidence/verification standard.
