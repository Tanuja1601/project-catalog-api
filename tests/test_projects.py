def test_project_crud_flow(client):
    create_response = client.post(
        "/api/v1/projects",
        json={
            "title": "Portfolio API",
            "summary": "Built a production-style API to showcase backend engineering capability.",
            "tech_stack": ["FastAPI", "SQLAlchemy", "Pytest"],
            "repo_url": "https://github.com/example/portfolio-api",
            "live_url": "https://example.com/api/projects/1",
            "is_featured": True,
        },
    )

    assert create_response.status_code == 201
    created_project = create_response.json()
    project_id = created_project["id"]
    assert created_project["title"] == "Portfolio API"

    list_response = client.get("/api/v1/projects")
    assert list_response.status_code == 200
    assert len(list_response.json()) == 1

    get_response = client.get(f"/api/v1/projects/{project_id}")
    assert get_response.status_code == 200
    assert get_response.json()["id"] == project_id

    update_response = client.put(
        f"/api/v1/projects/{project_id}",
        json={
            "title": "Portfolio API Updated",
            "summary": "Updated showcase API with cleaner contracts and documentation.",
            "tech_stack": ["FastAPI", "SQLAlchemy", "Docker"],
            "repo_url": "https://github.com/example/portfolio-api",
            "live_url": "https://example.com/api/projects/1",
            "is_featured": False,
        },
    )
    assert update_response.status_code == 200
    assert update_response.json()["title"] == "Portfolio API Updated"

    delete_response = client.delete(f"/api/v1/projects/{project_id}")
    assert delete_response.status_code == 204

    missing_response = client.get(f"/api/v1/projects/{project_id}")
    assert missing_response.status_code == 404