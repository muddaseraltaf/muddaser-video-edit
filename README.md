# Muddaser Video Editing Skills

Portable instructions, motion recipes and practical helpers for English/Urdu video editing. Built from iterative reviews and reference studies: strong openings, source-grounded visuals, purposeful half/full screens, smooth movement and selective highlights.

This repository preserves the creative decisions and workflow so a new AI does not need the old conversation. It is an agent skill, not an automatic one-click editor. Actual editing still requires a capable AI, local video tools, a renderer and review.

## Use with another AI
Give it the repository folder and this prompt:

> Read SKILL.md. Use this workflow and its saved creative direction. Check the available tools, resume any existing projects, and edit the video in source/. Save the finished MP4 in output/ and keep a portable project handoff. Ask only for genuinely missing information.

- **Codex:** copy this whole directory into `~/.codex/skills/muddaser-video-editing-skills/`, or use the folder directly in your task. Reload skill discovery if needed.
- **Claude Code:** copy the directory into `~/.claude/skills/muddaser-video-editing-skills/`, or ask Claude to read its SKILL.md directly. The small CLAUDE.md points to the same source of truth.
- **Other agents:** read SKILL.md and follow its relative links. If the agent cannot execute tools, it can prepare a plan, but cannot truthfully claim a rendered video.

No Codex-only tool names, personal absolute paths, private footage or model weights are required by the instructions.

## Setup
Read [setup](references/setup.md). Python 3.9+, Node 22+ / npm, FFmpeg/FFprobe are the baseline. Run:

```sh
npm ci
python3 scripts/doctor.py
python3 scripts/init_workspace.py /path/to/video-workspace
```

The npm dependency pins the established Hyperframes baseline rather than silently tracking latest. Urdu/English local Whisper models are optional large downloads handled separately. A timestamped transcript can also be imported.

Use `source/` for raw footage, `samples/` for reference videos and companion material near its source. `projects/` stores analysis/editable work; `output/` holds finished files. Keep these private folders outside the skill install directory when practical.

## What is included
- One short skill entry point, focused references and an additive benchmark library.
- Intake/contact-sheet helper, cached transcript import/local transcription, dependency checker and workspace initializer.
- Small GSAP motion helpers for framed handoffs, masked phrases, guided highlights and curved travel.
- Project handoff schema and verification expectations.
- Smoke tests using synthetic media; no private samples or exported personal videos.

```sh
npm test
```

## GitHub
This is prepared as a standalone repository. Its ignore rules exclude media, transcripts, generated projects, model weights, local paths/state and dependencies. Review the file list before publishing. Select a license for your original package when publishing; no license choice has been made on your behalf. Upstream packages have their own licenses and are installed separately; see [provenance](references/provenance.md).

Existing edits and original reference videos stay in the old workspace. To continue one of those projects on another computer, transfer that private project and its source/assets separately, using the handoff instructions. Installing this skill alone does not transfer the footage or models.
