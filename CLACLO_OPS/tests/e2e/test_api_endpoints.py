from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.models import Base, University, Survey

# Initialize the TestClient
client = TestClient(app)

# Setup a test database
def setup_module(module):
    global transaction, connection, engine, TestingSessionLocal

    # Create an in-memory SQLite database for testing
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)

    # Begin a non-ORM transaction
    connection = engine.connect()
    transaction = connection.begin()

    # Bind an individual session to the connection
    db = TestingSessionLocal(bind=connection)
    app.dependency_overrides[app.dependencies.get_db] = lambda: db

def teardown_module(module):
    app.dependency_overrides.clear()

    # Roll back the overall transaction and close the connection
    transaction.rollback()
    connection.close()
    engine.dispose()

def test_university_and_survey_flow():
    # Create a new university
    response = client.post("/universities/", json={"name": "Test University"})
    assert response.status_code == 200
    university_id = response.json()['id']

    # Create a new survey associated with the university
    response = client.post("/surveys/", json={"title": "Student Feedback", "university_id": university_id})
    assert response.status_code == 200
    survey_id = response.json()['id']

    # Retrieve the created survey
    response = client.get(f"/survey-reports/{survey_id}")
    assert response.status_code == 200
    assert response.json()['title'] == "Student Feedback"

    # Get all survey reports for the university
    response = client.get(f"/university/{university_id}/survey-reports")
    assert response.status_code == 200
    assert any(s['id'] == survey_id for s in response.json())

# Additional tests can be added in a similar manner to test other functionalities.
