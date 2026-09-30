from fastapi.testclient import TestClient
from app.main import app
from app.data import AREAS
from app.risk import calculate

client=TestClient(app)

def test_core_routes():
    for path in ["/api/health","/api/cyclone/current","/api/cyclone/track","/api/areas","/api/risk","/api/infrastructure","/api/priorities","/api/model-info","/api/data-sources"]:
        assert client.get(path).status_code==200

def test_risk_bounded_and_simulation_recalculates():
    base=client.post("/api/simulate",json={"area_id":"nagapattinam","wind_kmh":140,"rainfall_mm":155,"pressure_hpa":950}).json()["results"]
    changed=client.post("/api/simulate",json={"area_id":"nagapattinam","wind_kmh":180,"rainfall_mm":220,"pressure_hpa":930}).json()["results"]
    assert 0 <= base["overall"] <= 100
    assert changed["overall"] > base["overall"]

def test_validation_and_unknown_area():
    assert client.post("/api/predict",json={"wind_kmh":999}).status_code==422
    assert client.post("/api/simulate",json={"area_id":"missing"}).status_code==404

def test_ai_demo_fallback_and_validation():
    result=calculate(AREAS[0])
    response=client.post("/api/ai/explain",json={"result":result,"language":"English"})
    assert response.status_code==200
    assert "prototype" in response.json()["explanation"].lower()
    assert client.post("/api/ai/explain",json={"result":{},"language":"English"}).status_code==422
