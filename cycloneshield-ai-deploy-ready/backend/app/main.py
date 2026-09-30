import os
from pathlib import Path
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from .data import AREAS, TRACK
from .risk import calculate, rank

app = FastAPI(title="CYCLONEShield AI API", version="0.1.0")
app.add_middleware(CORSMiddleware, allow_origins=os.getenv("ALLOWED_ORIGINS","http://localhost:5173").split(","), allow_methods=["*"], allow_headers=["*"])

class Scenario(BaseModel):
    area_id: str | None = None
    wind_kmh: float = Field(default=140, ge=0, le=350)
    rainfall_mm: float = Field(default=155, ge=0, le=1000)
    pressure_hpa: float = Field(default=950, ge=800, le=1100)

class ExplainRequest(BaseModel):
    result: dict
    language: str = Field(default="English", pattern="^(English|Tamil|Hindi)$")

def area_by_id(area_id: str):
    for area in AREAS:
        if area["id"] == area_id:
            return area
    raise HTTPException(404, "Unknown area_id")

@app.get("/api/health")
def health(): return {"status":"ok","data_mode":"DEMO / PROTOTYPE DATA"}

@app.get("/api/cyclone/current")
def cyclone(): return {"name":"Demo Cyclone","mode":"DEMO / PROTOTYPE DATA","wind_kmh":140,"pressure_hpa":950,"rainfall_mm":155,"direction":"West-northwest","note":"Illustrative scenario; not a live storm or forecast."}

@app.get("/api/cyclone/track")
def track(): return {"track":TRACK,"mode":"DEMO / PROTOTYPE DATA"}

@app.get("/api/areas")
def areas(): return {"areas":AREAS,"mode":"DEMO / PROTOTYPE DATA"}

@app.get("/api/risk")
def risks(): return {"results":rank(AREAS),"mode":"DEMO / PROTOTYPE DATA"}

@app.get("/api/infrastructure")
def infrastructure(): return {a["id"]:{"area":a["name"],"assets":a["assets"]} for a in AREAS}

@app.get("/api/priorities")
def priorities(): return {"priorities":rank(AREAS)[:5],"mode":"DEMO / PROTOTYPE DATA"}

@app.post("/api/predict")
def predict(s: Scenario):
    if s.area_id: return calculate(area_by_id(s.area_id),s.wind_kmh,s.rainfall_mm,s.pressure_hpa)
    return {"results":rank(AREAS,s.wind_kmh,s.rainfall_mm,s.pressure_hpa)}

@app.post("/api/simulate")
def simulate(s: Scenario):
    area=area_by_id(s.area_id) if s.area_id else None
    return {"results":calculate(area,s.wind_kmh,s.rainfall_mm,s.pressure_hpa) if area else rank(AREAS,s.wind_kmh,s.rainfall_mm,s.pressure_hpa),"scenario":{"wind_kmh":s.wind_kmh,"rainfall_mm":s.rainfall_mm,"pressure_hpa":s.pressure_hpa},"mode":"DEMO / PROTOTYPE DATA"}

@app.post("/api/ai/explain")
async def explain(req: ExplainRequest):
    result=req.result
    if not all(k in result for k in ("area","impact","infrastructure","population_exposure","overall","level")):
        raise HTTPException(422,"Result must contain structured risk fields")
    key=os.getenv("GEMINI_API_KEY")
    if key:
        model=os.getenv("GEMINI_MODEL","gemini-2.0-flash")
        prompt=(f"Explain in {req.language} the provided prototype risk values for a disaster-preparedness audience. "
                "Use only the supplied values and factors. Do not invent forecasts, facts, advice as official orders, "
                "or new numbers. State this is a prototype estimate. Return concise plain text. DATA="+str(result))
        try:
            async with httpx.AsyncClient(timeout=20) as client:
                response=await client.post(f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}",json={"contents":[{"parts":[{"text":prompt}]}]})
            response.raise_for_status()
            text=response.json()["candidates"][0]["content"]["parts"][0]["text"]
            return {"explanation":text,"provider":"Google Gemini","label":"AI-generated explanation"}
        except Exception:
            pass
    return {"explanation":f"{result['area']} has a {result['level'].lower()} prototype risk estimate of {result['overall']}/100. Impact ({result['impact']}), infrastructure vulnerability ({result['infrastructure']}), and population exposure ({result['population_exposure']}) contribute according to the published prototype weights. These are illustrative estimates, not official hazard information.","provider":"Deterministic demo fallback","label":"Demo explanation (Gemini not configured)"}

@app.get("/api/model-info")
def model_info(): return {"name":"Transparent prototype weighted scoring","trained_ml":False,"accuracy":None,"weights":{"impact":0.4,"infrastructure":0.35,"population":0.25},"note":"No scientifically validated labels available; no predictive accuracy claim."}

@app.get("/api/data-sources")
def sources(): return {"mode":"DEMO / PROTOTYPE DATA","sources":[{"name":"Hack2skill event challenge brief","url":"https://hack2skill.com/event/codeforcommunities2","use":"Requirements only"},{"name":"OpenStreetMap","url":"https://www.openstreetmap.org/","use":"Potential infrastructure layer; not downloaded into this demo"},{"name":"NASA SRTM / Earthdata","url":"https://www.earthdata.nasa.gov/data/catalog/lpcloud-srtmgl1-003","use":"Potential elevation input; not downloaded into this demo"},{"name":"WorldPop","url":"https://www.worldpop.org/","use":"Potential population raster; verify dataset license/metadata before use"},{"name":"India Meteorological Department","url":"https://mausam.imd.gov.in/","use":"Authoritative weather/cyclone information; no live feed connected"},{"name":"Google Earth Engine","url":"https://earthengine.google.com/","use":"Required-track satellite integration target; credentials/data pipeline not configured"}]}


# Serve the built React app from the same service when present (Docker / Cloud Run deployment).
_static = Path(__file__).resolve().parent.parent / "static"
if _static.is_dir():
    app.mount("/", StaticFiles(directory=_static, html=True), name="frontend")
