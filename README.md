# GOOBTV STUDIO — WRONGSIDE

## NEW: Instant browser-based 3D preview

Open **[index.html](index.html)** in the repository to see the source for the real-time 3D player. It uses Three.js via a CDN and animates Pip, the sidewalk, and the camera in WebGL. **No GitHub Actions run is needed.**

### Publish to your phone using free GitHub Pages

1. Open this repository on GitHub.
2. Go to **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**.
4. Select **main** and **/(root)**, then **Save**.
5. After GitHub Pages finishes deploying, open: https://motionsupplyco.github.io/GOOBTV-STUDIO/

The player loads Three.js from a public CDN, so it needs an internet connection. GitHub Pages deployment must be enabled by the repo owner; a commit alone does not publish a site.

### Preview features
- Live 3D character movement, camera views, timeline scrubbing, fullscreen
- Shot 01C test: 10 seconds
- 16:9 landscape
- No rendered MP4 yet; no voice recording or final character rigs yet

### Important
This is a rough prototype with simple geometry and placeholder subtitles. The existing Blender workflows remain in the repository but are no longer needed to preview this scene.

## Previous experimental Blender workflows
Earlier attempts rendered frames on GitHub Actions and were slow. Those remain available for comparison, but do not use them for quick iteration.
