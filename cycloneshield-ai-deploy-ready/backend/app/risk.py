"""Transparent prototype scoring. Not trained ML and not an official hazard model."""
WEIGHTS = {"impact": 0.40, "infrastructure": 0.35, "population": 0.25}

def level(score: float) -> str:
    return "HIGH" if score >= 67 else "MEDIUM" if score >= 34 else "LOW"

def calculate(area: dict, wind_kmh: float = 140, rainfall_mm: float = 155, pressure_hpa: float = 950) -> dict:
    # Weather factors are normalized around the editable demo baseline. Keeping
    # weather as an additive adjustment avoids saturating every coastal area at 100.
    wind = min(1.25, max(0.4, wind_kmh / 140))
    rain = min(1.25, max(0.4, rainfall_mm / 155))
    pressure = min(1.2, max(0.5, (1010 - pressure_hpa) / 60))
    baseline = area["wind_factor"]*0.37 + area["rain_factor"]*0.38 + area["pressure_factor"]*0.25
    weather_delta = ((wind-1)*area["wind_factor"]*0.37 + (rain-1)*area["rain_factor"]*0.38 + (pressure-1)*area["pressure_factor"]*0.25) * 0.8
    spatial = max(0, 20-area["coast_km"])*0.12 + max(0, 30-area["track_km"])*0.06 + max(0, 15-area["elevation_m"])*0.08
    impact = min(100, max(0, baseline + weather_delta + spatial))
    infrastructure = min(100, area["infrastructure_density"] * 0.45 + sum(area["assets"].values()) / len(area["assets"]) * 0.55)
    population = min(100, area["population_density"] * (0.7 + max(0, 15-area["elevation_m"])/50) * (1 + max(0, 15-area["coast_km"])/100))
    overall = round(impact*WEIGHTS["impact"] + infrastructure*WEIGHTS["infrastructure"] + population*WEIGHTS["population"])
    return {"area_id":area["id"],"area":area["name"],"impact":round(impact),"infrastructure":round(infrastructure),"population_exposure":round(population),"estimated_exposed_population":None,"overall":overall,"level":level(overall),"weights":WEIGHTS,"factors":{"wind_kmh":wind_kmh,"rainfall_mm":rainfall_mm,"pressure_hpa":pressure_hpa,"distance_to_coast_km":area["coast_km"],"distance_to_track_km":area["track_km"],"elevation_m":area["elevation_m"]},"assets":area["assets"],"suggestions":["Review evacuation routes and access constraints","Inspect critical infrastructure readiness","Check shelter capacity and emergency supplies"]}

def rank(areas: list, wind_kmh: float = 140, rainfall_mm: float = 155, pressure_hpa: float = 950) -> list:
    return sorted((calculate(a, wind_kmh, rainfall_mm, pressure_hpa) for a in areas), key=lambda r:r["overall"], reverse=True)
