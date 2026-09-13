# Cutouts and dimensional motion

Load when the spoken idea benefits from layers, a reveal or a product view. These are proposed constructions inferred from reference frames, not recovered source projects or tested presets. Exact creator tools and easing curves are unknown. Aesthetic timing and opening priorities stay in [creative direction](creative-direction.md).

## Choose the simplest sufficient method
| Explanatory job | Method | Required assets / constraint |
|---|---|---|
| Introduce a person, object or idea | Editorial cutout collage | Relevant transparent subject, supporting shape/type, coherent shadow |
| Reveal what is inside or behind | Hinged cutout | Separate body, lid, interior, foreground lip and revealed content |
| Give a statement depth | Perspective poster | Backing plane, color field, subject breaking the boundary, foreground detail; mild shared viewpoint movement |
| Explain messages or a workflow | Floating interface layers | Readable cards attached to a device/context; real sourced UI when making product claims |
| Show unseen sides or internal construction | Actual 3D or matching footage | Suitable geometry/parts or licensed pre-rendered views; a single PNG is insufficient |
| Move from concept to proof | Object → demonstration | Shared anchor/window; object yields to relevant recording, which expands and holds |
| Connect short ideas | Minimal shape sequence | Persistent dot/ring/frame changes state with the phrase; collage is optional |

## Prepare assets before animation
Use genuine transparency, not a baked checkerboard. Leave padding around hair, hands and projecting parts; provide enough resolution for the largest on-screen scale. Inspect edges on both light and dark surfaces for halos and clipped details. Use available authorized masking/generation tools and record provenance. A generated illustrative cutout must not masquerade as a real screenshot or factual product evidence.

For articulation, prepare separate parts registered to the same coordinate system. Record bounds, pivot and depth order. Test the closed pose first: seams must join without jumps or doubled edges. An intact photograph does not contain the hidden interior; obtain or deliberately illustrate that missing part before planning a reveal.

Use a hierarchy such as `scene → depth layer → subject motion → asset`. Assign each transform property to one owner: camera drift on the scene, parallax on depth wrappers, entrance/hinge motion on subject or part wrappers. Attach labels and accessories to the part they follow. Keep shadows and occluding lips in the appropriate sibling layers so they can move differently. A useful initial stack is background → supporting shape/type → shadow → subject → foreground occluder → essential text; adjust to actual geometry.

## Hinged reveal with occlusion
Establish the closed object → rotate its lid around the seam → hold the opening → raise the revealed subject from behind the front lip. The dark interior stays behind the body; the emerging subject passes behind the foreground lip instead of fading into existence over it. Place the pivot at the hinge, not the lid's center. Parent any strings/attachments to the relevant moving assembly.

On return, lower the revealed subject fully behind the lip before closing the lid, then move the assembled object away. Inspect the partly open pose and the moment of concealment for leaking content, duplicate edges or detached parts. The paper-puppet benchmark suggests this layered construction; it does not require a full 3D skull model to communicate an illustrative reveal.

## Perspective poster and floating layers
Design the final readable pose first. Start from a detail or mild tilt, then pull back/settle into the composition. Let a color field establish the space, a cutout resolve next, and the key phrase settle last. A subject extending beyond a backing panel helps establish overlapping layers without adding gratuitous rotation.

Give layers different travel amounts: background small, supporting layers moderate, foreground largest. A starting ratio such as 0.25 / 0.6 / 1 is a tuning suggestion, not a measurement from the samples. Keep text stable during reading. Use transition blur briefly and restore sharpness for the hold. Float can sustain a pose gently; it should not compete with a principal reveal.

For CSS planes, use a shared perspective parent and intentional transform origins; inspect stacking and overflow clipping in the actual renderer. Larger perspective distance weakens the depth effect. Perspective transforms project flat layers; they do not create unseen object surfaces. See the [MDN perspective reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/perspective).

Make shadows agree with lighting and motion. Use an alpha-following shadow for a floating cutout or a separate contact shadow for a standing subject. As it rises from a surface, soften/broaden/lighten the contact shadow; reverse on landing. Avoid doubling a shadow already baked into the asset. Small rotation, restrained drift and consistent contact usually convey more depth than large random spins.

## Actual product 3D
The camera benchmark shows rear/side/front surfaces, changing highlights and an exploded assembly. To reproduce that kind of view truthfully, use an appropriate model with separate parts or matching licensed rendered footage. Establish the product → show a relevant detail → separate related components along meaningful local axes → hold the explanation → reassemble to saved transforms. Keep part identity, camera target and lighting coherent; stagger related groups rather than scattering them randomly.

Check available assets and renderer capabilities before promising a full orbit or exploded view. An available 3D renderer can supply a deterministic insert for the video composition; this skill does not install one or include models. If geometry is unavailable, use a restrained cutout or clearly illustrative schematic. Do not fabricate factual internal structure. Adapt fast product-montage cuts to the narration and reading time rather than copying their speed.

## Plan and review
In DESIGN.md record the spoken beat, explanatory job, asset source, layers/pivots and enter/hold/exit sequence. Reuse existing motion helpers only where they fit; do not claim a recipe is implemented merely because its guide exists.

Inspect a dense sequence around overlap, hinge opening, maximum tilt and return. Check the exported result for cutout edges at peak scale, occlusion, shadow attachment, readable shaped Urdu, face crops and conflicting transforms. Keep the effect only if its state change helps explain the beat. Report new implementations as trials until reviewed.
