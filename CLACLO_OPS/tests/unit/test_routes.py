

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from ...app.main import app
#from ...app.database import Base, get_db
from app.main import app
from app.database import Base, get_db
from app.models import University

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_university():
    response = client.post("/universities/universities", json={"name": "Test University"})
    assert response.status_code == 200
    assert response.json()['name'] == "Test University"

def test_create_university_duplicate():
    client.post("/universities/universities", json={"name": "Test University"})  # Initial creation
    response = client.post("universities/universities/", json={"name": "Test University"})  # Try to create duplicate
    assert response.status_code == 400
    assert "already exists" in response.json()['detail']

def test_activate_university():
    university = client.post("/universities/universities/4/activate", json={"name": "Test University"})
    university_id = 4
    response = client.patch(f"universities/universities/{university_id}/activate")
    assert response.status_code == 200
    assert response.json()['is_active'] == True


def test_deactivate_university():
    university = client.post("/universities/universities/1/deactivate", json={"name": "Test University"})
    university_id = 4
    response = client.patch(f"universities/universities/{university_id}/activate")
    assert response.status_code == 200
    assert response.json()['is_active'] == False