# ML and validation plan

There is no trained ML model in this prototype. Because we do not have verified labeled storm-area outcomes, training a Random Forest/XGBoost model or reporting accuracy would be misleading. Present scores as a transparent deterministic prototype scoring baseline, not an ML prediction.

Future training requires event-by-area labels (e.g. observed flood depth/damage, service interruption, validated exposure), consistent time-aligned meteorology, track uncertainty, elevation, population and asset data. Split validation by cyclone event and time (not random rows) to prevent leakage from neighboring areas or repeated track observations. Compare against simple baselines; assess calibration, recall for severe impacts, geographic fairness, missingness, and uncertainty. Report event-held-out results and data provenance. Retrain only with documented governance and expert review.
