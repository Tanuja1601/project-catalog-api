def test_health_endpoint(client):
    response = client.get("/api/v1/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_version_endpoint(client):
    response = client.get("/api/v1/version")

    assert response.status_code == 200
    payload = response.json()
    assert payload["name"] == "Portfolio API Showcase"
    assert payload["version"] == "0.1.0"
