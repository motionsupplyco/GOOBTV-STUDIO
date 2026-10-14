# WRONGSIDE — 3D Production Rebuild (Research + Implementation Contract)

## Decision
Retire the old primitive Pip demo as the quality target. Keep it only as an engineering fallback. No more claiming a prototype is a finished episode.

## Findings (2026-10-14)
- Three.js supports GLTFLoader, AnimationMixer, crossfading and facial morph targets: https://threejs.org/examples/webgl_animation_skinning_morph.html
- Adobe Mixamo animations and characters are free for commercial film use with Adobe ID, but its automatic rigging supports **bipedal humanoids only**. https://helpx.adobe.com/creative-cloud/faq/mixamo-faq.html
- Kenney Animated Characters 3 has CC0 rigged human/zombie characters and idle/run/jump, but is **not a match for Pip**. https://kenney-assets.itch.io/animated-characters-3
- For WRONGSIDE's original raccoon/creature/sign/cloud designs, the right path is **original meshes + custom rigs**, not pretending stock human assets are the finished cast.
- Public GitHub Pages redistributes raw assets; do not upload Mixamo files to a public repo without reviewing redistribution restrictions. Prefer original assets or CC0 assets.

## Build gates
1. **Visual design approval:** produce canonical turnaround (front, side, back) for Pip, Bongo, Ziggy, Mr. Drizzle; proportion, face shapes, clothing, material palette; user approval before implementation.
2. **Production asset:** original Blender mesh and skeleton for Pip; GLB export; eyes/mouth controls and eyelid expressions. No unlicensed assets.
3. **Motion:** authored idle, walk, run, trip, fall, stand, talk; blend smoothly using Three.js AnimationMixer. Check feet don't skate.
4. **Town:** modeled street, curb, storefronts, foliage, props; lighting, shadows, depth, stylized textures. Phone performance target tested on actual iPhone.
5. **Audio:** English voice tracks per character (with permission), SFX, music, dialogue timing, lip sync; browser speech synthesis is temporary only.
6. **Shot quality:** a polished 20–30 second story moment approved on iPhone before attempting 15 minutes.
7. **Episode assembly:** timed shots and dialogue, reusable assets, subtitles, audio mixing, export path; 15-minute episode only after gate 6 passes.

## File layout
- assets/characters/pip.glb (not yet built)
- assets/characters/bongo.glb (not yet built)
- assets/characters/ziggy.glb (not yet built)
- assets/characters/drizzle.glb (not yet built)
- assets/environments/wrongside_street.glb (not yet built)
- assets/audio/ (not yet recorded)
- player/ (real-time 3D playback; current index.html is prototype only)

## Hard truths
- No free web library automatically generates high-quality original rigged characters with professional voice acting.
- Rigging/modeling and quality review are real work, even with free tools.
- A 15-minute show should not be built from placeholders. First prove one strong shot.
- Never spend paid credits without user approval.
