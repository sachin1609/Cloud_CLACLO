import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import MagicMock, patch
from app.main import app
from app import models, schemas

client = TestClient(app)

@pytest.fixture
def mock_db_session():
    # Mock the SQLAlchemy Session
    db_session = MagicMock(spec=Session)
    db_session.add = MagicMock()
    db_session.commit = MagicMock()
    db_session.refresh = MagicMock()
    db_session.query = MagicMock()
    return db_session

def test_create_survey(mock_db_session):
    with patch("app.api.router.get_db", return_value=mock_db_session):
        response = client.post("/surveys/", json={"title": "Student Feedback", "university_id": 1})
        assert response.status_code == 200
        assert "id" in response.json()

def test_create_survey_report(mock_db_session):
    with patch("app.api.router.get_db", return_value=mock_db_session):
        response = client.post("/survey-reports/", json={"survey_id": 1, "details": "Report for Student Feedback"})
        assert response.status_code == 200
        assert "id" in response.json()

def test_get_survey_report(mock_db_session):
    # Mocking the return value for a survey report retrieval
    expected_report = models.SurveyReport(id=1, survey_id=1, details="Report for Student Feedback")
    mock_db_session.query.return_value.filter.return_value.first.return_value = expected_report
    
    with patch("app.api.router.get_db", return_value=mock_db_session):
        response = client.get("/survey-reports/1")
        assert response.status_code == 200
        assert response.json()['details'] == "Report for Student Feedback"

def test_get_university_survey_reports(mock_db_session):
    # Mocking the return value for multiple survey reports retrieval
    expected_reports = [
        models.SurveyReport(id=1, survey_id=1, details="Report 1"),
        models.SurveyReport(id=2, survey_id=2, details="Report 2")
    ]
    mock_db_session.query.return_value.join.return_value.filter.return_value.all.return_value = expected_reports
    
    with patch("app.api.router.get_db", return_value=mock_db_session):
        response = client.get("/university/1/survey-reports")
        assert response.status_code == 200
        assert len(response.json()) == 2
        assert response.json()[0]['details'] == "Report 1"
        assert response.json()[1]['details'] == "Report 2"

def test_survey_report_not_found(mock_db_session):
    # Return None when the survey report is not found
    mock_db_session.query.return_value.filter.return_value.first.return_value = None

    with patch("app.api.router.get_db", return_value=mock_db_session):
        response = client.get("/survey-reports/999")
        assert response.status_code == 404
        assert response.json()['detail'] == "Survey report not found"

def test_university_survey_reports_not_found(mock_db_session):
    # Return empty list when no reports are found for the university
    mock_db_session.query.return_value.join.return_value.filter.return_value.all.return_value = []
    
    with patch("app.api.router.get_db", return_value=mock_db_session):
        response = client.get("/university/999/survey-reports")
        assert response.status_code == 404
        assert response.json()['detail'] == "No survey reports found for this university"
