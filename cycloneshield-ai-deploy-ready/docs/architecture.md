# Architecture

React/Vite dashboard -> FastAPI JSON API -> deterministic, configurable prototype scoring over a geographic area record. The map uses Leaflet with OpenStreetMap tiles and illustrative cyclone points. The explanation endpoint sends structured calculated values to Gemini only when `GEMINI_API_KEY` is configured; otherwise it returns a visibly labeled deterministic fallback.

Area records contain country, state, district, coordinates, proximity/elevation attributes, and illustrative inventory indices. The scoring code consumes features rather than district-specific conditionals. A future implementation should ingest versioned geospatial layers (administrative polygons, DEM, population rasters, exposure buffers, and verified infrastructure inventories) and preserve source lineage per feature.

## Challenge alignment and gaps

Problem 05 requires GEE satellite feeds, real-time meteorology, Gemini 3.7 Flash multimodal reasoning, surge simulation, rainfall damage pathways, critical-infrastructure exposure, and automated advisory dispatch. This MVP implements only the scenario-to-area scoring and grounded text explanation portions. It does not dispatch alerts, simulate hydrodynamics, read satellite imagery, or connect live meteorological data. Automated dispatch is intentionally omitted pending authority, validation, consent, and safety processes.
