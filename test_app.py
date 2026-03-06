from app import app

def test_home_status():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_home_content():
    client = app.test_client()
    response = client.get("/")
    assert response.data.decode() == "Hello from Web App!"

def test_invalid_route():
    client = app.test_client()
    response = client.get("/about")
    assert response.status_code == 404