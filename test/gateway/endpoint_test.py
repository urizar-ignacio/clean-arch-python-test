from io import BytesIO
import pytest 
from src.app import app

@pytest.fixture()
def app_setup():
    app.config.update(
        {
            "TESTING": True
        }
    )

    yield app

@pytest.fixture()
def client(app_setup):
    return app_setup.test_client()

def generate_sample_jobs_file():
    sample_file_content = b"""1,Job 1\n2,Job 2\n3,Job 3"""
    return BytesIO(sample_file_content)

def test_get_jobs(client):
    response = client.get("/api/jobs/")
    assert response.status_code == 200

def test_post_jobs_file(client):
    response = client.post(
        "/api/jobs/", 
        data={
            "file": (generate_sample_jobs_file(), "sample_file.csv")
        },
        content_type='multipart/form-data'
    ,)
    assert response.status_code == 200

def test_post_jobs_without_file(client):
    response = client.post("/api/jobs/", data={})
    assert response.status_code == 400
    assert response.json.get("BAD_REQUEST") == "No file attached to POST request"

def test_post_jobs_file_with_wrong_extension(client):
    response = client.post(
        "/api/jobs/", 
        data={
            "file": (generate_sample_jobs_file(), "sample_file.txt")
        },
        content_type='multipart/form-data'
    ,)
    assert response.status_code == 400
    assert response.json.get("BAD_REQUEST") == "File extension not supported. Must be .csv"

def test_post_jobs_file_with_empty_file(client):
    response = client.post(
        "/api/jobs/", 
        data={
            "file": (BytesIO(b""), "sample_file.csv")
        },
        content_type='multipart/form-data'
    ,)
    assert response.status_code == 400
    assert response.json.get("BAD_REQUEST") == "Empty file"

