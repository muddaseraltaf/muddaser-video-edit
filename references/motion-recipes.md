# Motion implementation
Read creative-direction.md for the canonical aesthetic and timing preferences. `assets/motion.js` is newly authored, renderer-neutral GSAP choreography; load GSAP first and pass a paused timeline. It does not place, play or trim media.

## Framed left handoff
`MuddaserMotion.handoff(tl, outgoing, incoming, time, width=1080)` shrinks/translates complete wrappers, overlaps arrival, then expands. Each wrapper must have its own safe crop; z-order should show incoming content rather than hide it behind an outgoing opaque panel. Test both direction/actor roles, shared midpoint and final pose. Defaults reproduce the established 1.58s sequence; adjust when distance/reading calls for it.

## Phrase mask
`phrase(tl, outer, ink, underline, start, end)` reveals a whole phrase inside an overflow-hidden wrapper. Provide enough vertical space for Urdu glyphs, with no per-letter spans. This helper enforces enough duration for enter/hold/exit; it does not validate wording or create captions.

## Guided highlight
`highlight(tl, selector, start, duration)` grows an overlay from its CSS transform-origin. Set source-mapped rectangle coordinates and reading direction before animation. Highlight geometry must transform with the screenshot. Establish context, crop to relevant text, sweep only the spoken passage, hold, then return. Never replace source text with a fabricated recreation.

## Curved travel
`arc(tl, selector, start, from, control, to, duration)` samples a quadratic path into one GSAP keyframe tween using a smooth progression. New layers can settle after the main object. Avoid another simultaneous tween controlling the same properties. Seed randomness or use finite deterministic phases.

## Further recipes
- Persistent diagram: name states, keep object IDs stable, change boundary/connection/state at the narrated action. One coherent diagram can support a long passage.
- Evidence focus: sharp crop above a dimmed/blurred contextual copy; align both precisely. Keep source attribution readable.
- Parallax: low background amplitude, medium supporting layer, larger foreground movement; stop before readability suffers. Never animate all layers equally just to make them move.
- Screenshot→demonstration→screenshot: keep asset identity, enlarge only relevant media, retain suitable real audio and attribution, return to the passage being explained.

These are starting tools, not a fixed card template. Validate rendered output; importing a helper is not proof of good editing.
