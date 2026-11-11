from app import app


def test_health():
    with app.test_client() as client:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.get_json()["status"] == "healthy"


def test_home():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.get_json()["servico"] == "SCN API"
