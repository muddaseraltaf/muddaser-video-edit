# Editing and portable project state

## Intake and planning
1. Identify the requested input in source/. Inspect metadata, orientation, HDR/color, audio, scene changes and representative frames. `scripts/intake.py` makes a basic contact sheet; six frames are an initial look, not a deep review.
2. Read/create timestamped speech using transcription.md. Review uncertain words and meaningful pauses. Propose frame-aligned silence/mistake cuts; preserve qualifiers and natural breaths. Do not classify all gaps as mistakes or deliberately requested speech cuts as silence.
3. Write a compact DESIGN.md: hook, spoken beats, insert job/source, diagram states, chosen layout/type/palette/movement and readable holds. Use benchmark-library to choose techniques, not to copy another video's claims.
4. Map all graphics and highlighted phrases to the edited timeline. Keep source-to-output ranges. Include small cut handles and audio fades where appropriate. Preserve the original source.

## Implement and verify
Hyperframes/GSAP integration is described in motion-recipes.md. Normalize source geometry/color before composing. iPhone rotation/HLG needs explicit inspection: an output tagged Rec.709 is not by itself proof of correct tone mapping. Use an actual HDR-aware conversion (FFmpeg with needed filters or a native platform pipeline), inspect tone/skin/crop, and preserve source. Do not silently substitute a filter if the required converter is missing.

Keep the media crop separate from animated wrappers; use deterministic seekable animation. Choose relevant local/authorized online assets and record provenance. Do not publish or upload merely because the skill is installed.

Run the renderer's lint/runtime/layout checks and strict render. Inspect first 0.5/1/3/5/10 seconds, significant layout changes, main inserts and last frame. Check crops/highlights at phone scale, layer order between speaker and overlays, and uncertain movement in a short playback sequence where possible. Inspect a contact sheet made from the exported MP4 as well as composition snapshots. Measure duration, resolution, frame count, full decode, audio loudness/peak and end speech. Fresh ASR is warranted when cutting/mixing creates continuity uncertainty; unchanged decoded audio can reuse verified ASR. Disclose unperformed listening/playback rather than claiming it.

Write VERIFY.md with actual results, remaining limitations and whether review was sampled or continuous. Preserve each delivered version under output/. Retention/accuracy is not proven by a passing render.

## State for another AI
Keep these inside each private project, using paths relative to the workspace/project:
- `state.json`: schemaVersion, status, source path/hash, language, lastCompletedStage, output path, unresolved items and next actions.
- `DESIGN.md`: editorial decisions and current requested revision, not a whole conversation dump.
- `edit-decisions.json`: fps, duration, ordered source keep ranges and their output positions; record explicit tail cuts separately.
- `transcript.json` / `words.json`: source timestamps; separate edited timestamps/corrections with provenance.
- `assets/` plus source URL/license/date/context manifest for external material.
- editable composition and its dependency lockfile; render command/version.
- `VERIFY.md` and relevant checks.

Minimal state example (replace with actual values):
```json
{"schemaVersion":1,"status":"planned","source":{"path":"../../source/video.mov","sha256":"RECORD_ACTUAL_HASH"},"language":"ur","lastCompletedStage":"design","output":null,"unresolved":[],"nextActions":["Build composition from DESIGN.md"]}
```
The next AI reads state, verifies the source hash and dependencies, then resumes the next action. It does not redo completed work without a changed input or an unresolved concern. If moving the project, include media privately and repair paths; the public skill package is not a media backup.
