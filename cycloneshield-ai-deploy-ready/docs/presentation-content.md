# Pitch deck content (12 slides)

## 1. CYCLONEShield AI
Track-to-impact intelligence for anticipatory community resilience. Track: Problem 05, Resilience. Prototype pilot: coastal Tamil Nadu.

## 2. The problem
Cyclone response is often organized around hazard information, while local readiness decisions also need to consider which people and critical services could be exposed along a changing track.

## 3. The gap
Forecasts, maps, infrastructure inventories and population layers are separate inputs. Teams need a transparent way to explore their intersection. This prototype does not claim current products fail; it demonstrates an integration concept.

## 4. Our solution
A scenario dashboard connects a track scenario to area-level impact, infrastructure and population indices, ranked preparedness considerations, and a what-if control.

## 5. Innovation
Explainable track-to-vulnerability workflow: editable scenario -> geographic features -> component estimates -> transparent weighted composite -> priorities -> grounded language explanation.

## 6. Architecture
React + Leaflet interface, FastAPI validation/API, geographic feature records, deterministic risk engine, optional Gemini explanation. OSM basemap; source connectors are documented as future work.

## 7. AI/ML integrity
Gemini explains structured values but cannot set scores or invent forecasts. Demo uses deterministic scoring because labeled event outcomes are unavailable. No accuracy claim. Gemini connector is optional and server-keyed.

## 8. Infrastructure vulnerability
Road, bridge, hospital, shelter and power indices illustrate asset categories. Demo indices are synthetic. Pilot requires authoritative asset inventories, condition/capacity attributes and local validation.

## 9. Dashboard
Map, scenario metrics, priority queue and area breakdown are interactive. All displayed scenario and district inputs are labeled demo.

## 10. What-if simulation
Change wind/rain/pressure and recalculate actual model input. It is not a physical surge or rainfall-routing simulation.

## 11. Impact and scale
Geographic records are country/state/district/coordinate based, not district-coded business logic. Extend to other Indian coasts and BRICS contexts by ingesting local datasets, translation and governance workflows.

## 12. Deployability and next steps
Connect validated IMD and GEE feeds; add terrain/surge hydrodynamics and track uncertainty; validate historical events; field-review with authorities; security, privacy and alert governance. Pilot only after safety validation.
