# Data sources and provenance

| Dataset/source | URL | Coverage / period / units | License and use | Status here |
|---|---|---|---|---|
| Hack2skill Code for Communities 2 event page | https://hack2skill.com/event/codeforcommunities2 | Challenge and submission requirements; checked 2026-09-29 | Event page; not a data layer | Requirements only |
| IMD | https://mausam.imd.gov.in/ | India meteorology and cyclone information; products have product-specific time/units | Confirm specific product terms before reuse | Not connected; authoritative source candidate |
| OpenStreetMap | https://www.openstreetmap.org/ | Global mapped features; coverage/completeness varies; map display relies on public tile service | ODbL; attribution shown in map. Verify tile usage policy for deployment | Basemap only; no OSM assets downloaded |
| NASA SRTM / Earthdata | https://www.earthdata.nasa.gov/data/catalog/lpcloud-srtmgl1-003 | Near-global elevation product; elevation in meters | Check product-specific NASA data terms/attribution | Candidate only; no extraction |
| WorldPop | https://www.worldpop.org/ | Gridded population products vary by release/year and country | Check dataset-specific license and citation | Candidate only; demo density values synthetic |
| Google Earth Engine | https://earthengine.google.com/ | Geospatial platform and catalog feeds; coverage varies by selected asset | Asset-specific licensing/terms and account access apply | Not configured; challenge requirement gap |

Demo locations are approximate district-center coordinates for map illustration. All population density, asset indices, rainfall/wind susceptibility fields and scenario track fields in `backend/app/data.py` are synthetic and deliberately marked demo. Do not quote these as sourced statistics. No measured dataset license can be assigned to invented prototype attributes.
