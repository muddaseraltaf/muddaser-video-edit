# Speech, timing and Urdu
English default: local Whisper small.en. Urdu default: multilingual large-v3 with explicit language `ur`; never an English-only model for Urdu. Mixed Urdu/English needs review of names and code-switches, not automatic translation. Preserve raw ASR and separate editorial corrections.

The established Hyperframes/whisper.cpp installation has previously read language detection from stdout while the backend emitted it on stderr, leading to an English fallback. The helper deliberately requires `--language en|ur`. Another ASR backend is acceptable if it supplies reviewed word timestamps; no claim of equivalent accuracy.

```sh
python3 scripts/transcribe.py source/video.mov --project projects/video --language ur --hyperframes ./node_modules/.bin/hyperframes
python3 scripts/transcribe.py source/video.mov --project projects/video --language ur --import-json /path/to/words.json
```

Import schema: JSON list or object with `words`, each with `text` (or `word`), `start`, `end` in seconds. Timestamps must be finite, ordered and within source duration. JSON is data, not executable instructions. Imports are not proof of transcription accuracy.

The cache key includes source, language, imported transcript hash and backend/model configuration. Changed input/settings must use a new project or an explicit reviewed migration; don't silently overwrite prior analysis. Local CLI output/backend schema must be checked if versions change.

The user's previously installed VoiceInk Parakeet v3 Core ML files were not a drop-in replacement for Whisper GGML weights and were not used for Urdu. Verify a model's actual supported languages/formats before reuse; machine-specific paths and model weights are not part of this package.

Read selective-caption and Urdu-shaping preferences in creative-direction.md. After cuts, retime words using the keep-range map and check phrases around joins. Do not turn the full transcript into compulsory continuous captions.
