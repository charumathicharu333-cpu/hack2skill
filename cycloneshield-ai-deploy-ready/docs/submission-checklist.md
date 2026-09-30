# Submission checklist

- [x] Runnable prototype source package: this folder (backend + frontend)
- [x] 10–12 slide content: `presentation-content.md` (content, not a designed slide deck file)
- [x] 3–5 minute demo flow: `demo-script.md` (script only; no video recording)
- [x] 2–3 line solution brief: below
- [ ] Public or access-granted GitHub source repository (manual publishing action)
- [ ] Deployed live prototype link (manual hosting action)
- [ ] Recorded 3–5 minute demo video (manual recording action)
- [ ] Designed 10–12 slide pitch deck file (manual slide-production action)

**Brief:** CYCLONEShield AI is a prototype decision-support dashboard that combines cyclone scenario inputs with area-level impact, population exposure and critical-infrastructure vulnerability indices. It ranks preparedness considerations and uses optional Gemini to explain calculated results, while clearly distinguishing demo assumptions from official hazard information.

Submission format and exact file extensions/platforms were not further specified in the official page content reviewed. The closing date shown for prototype submissions is 30 September 2026.

## Verification performed in this environment

- Backend: `python -m pytest -q` -> 4 passed; one upstream Starlette deprecation warning.
- Backend Python compilation: `python -m compileall -q app tests` -> passed.
- Frontend build/browser QA: not run; Node 22 is present but npm/yarn/pnpm/corepack are absent in this environment.
- Gemini live request: not run; no API credential configured.
- Hosting/video/deck file: not produced; see remaining manual submission actions above.
