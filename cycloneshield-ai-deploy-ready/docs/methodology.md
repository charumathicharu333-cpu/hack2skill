# Prototype scoring methodology

All included location attributes are synthetic demo inputs, not sourced measurements. Every displayed score is an illustrative comparative index, not a probability, impact forecast, exposed-person count, or government classification.

Impact = baseline susceptibility (wind 37%, rainfall 38%, pressure 25%) plus a weather delta (0.8 times the weighted change from scenario baselines) and a small additive proximity/elevation term (coast 0.12 points/km within 20 km, track 0.06 points/km within 30 km, elevation 0.08 points/m below 15 m). Input baselines are 140 km/h, 155 mm, and 950 hPa. Each weather multiplier is bounded in code; final score is capped at 100 and floored at 0.

Infrastructure vulnerability = 45% illustrative infrastructure density + 55% mean of illustrative roads, bridges, hospitals, shelters, and power indices. Population exposure index = illustrative density scaled by illustrative lowland/coastal factors. Exact exposed population is deliberately `null`; no count is fabricated.

Overall prototype risk = 40% impact + 35% infrastructure vulnerability + 25% population exposure. Weights are unvalidated prototype assumptions, configurable in `backend/app/risk.py`. LOW <34, MEDIUM 34–66, HIGH >=67. These thresholds are for interface demonstration, not operational thresholds.

The what-if simulator changes actual scoring inputs and recalculates results. It is not a storm-track or hydrodynamic model. No supervised model was trained: valid labeled event outcomes were not present. No accuracy or predictive skill claim is made. Before any pilot, calibrate weights and validate against held-out historical events and local domain experts.
