from app import app

def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json == []

def test_post_task():
    client = app.test_client()
    response = client.post("/tasks", json={"task": "Test"})
    assert response.status_code == 201