# CYCLONEShield AI

Prototype decision support for exploring cyclone exposure, community exposure and critical infrastructure vulnerability. It is not an official forecast or warning system. All dashboard values are **DEMO / PROTOTYPE DATA** and must not be used for operational decisions.

## Run locally

Requires Python 3.10+ and Node.js 18+. In two terminals:

```sh
cd backend
python -m venv .venv
. .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

```sh
cd frontend
npm install
npm run dev
```

Open the Vite URL (normally http://localhost:5173). The UI uses `/api` proxy to FastAPI at port 8000. Backend tests: `cd backend && pytest`.

## What works

- Area-based deterministic risk and priority calculations, recalculated from changed wind/rain/pressure inputs.
- District selector, illustrative track map, component breakdown and prepared-response considerations.
- Risk explanation endpoint. Set `GEMINI_API_KEY` and optionally `GEMINI_MODEL` to use Google Gemini; otherwise a grounded, deterministic explanation is returned and labeled as demo fallback.
- Geographic records use country/state/district and coordinates; demo locations are not business-logic branches.
- API health, cyclone, track, areas, risk, infrastructure, priorities, prediction, simulation, AI explanation, model info and source metadata.

## Key caveats

The included district features are illustrative synthetic values, not measured district statistics. The event challenge calls for GEE satellite feeds, meteorological data and Gemini multimodal reasoning; this MVP does not yet connect GEE, live IMD feeds, official infrastructure inventories, or satellite-derived flood/surge models. Gemini explains provided structured fields only; it does not calculate risk or generate a forecast. No accuracy claim is made. See `docs/` for sources, assumptions and the gap to a field pilot.

## Event package checklist

The official event page requests a source-code repository (public or access granted), a 3–5 minute demo video, a 10–12 slide pitch deck, a 2–3 line solution description, and a deployed prototype link. This folder provides source and written presentation/demo content; no public repository, hosted deployment, or recorded video was created. These remain manual submission actions. Event page: https://hack2skill.com/event/codeforcommunities2 (checked 2026-09-29); prototype submission phase lists September 30, 2026 as closing date.

## Disclaimer

This prototype is intended for research and demonstration purposes. It does not replace official weather forecasts, government warnings, emergency-management authorities, or professional disaster-response decisions.
