import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, University, Survey
from app.schemas import UniversityCreate, SurveyCreate

# Set up the database engine and session for testing
@pytest.fixture(scope="module")
def test_db():
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# Utility function to add a university to the test database
def create_university(db, name):
    university = University(name=name)
    db.add(university)
    db.commit()
    db.refresh(university)
    return university

# Utility function to add a survey to the test database
def create_survey(db, title, university_id):
    survey = Survey(title=title, university_id=university_id)
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey

# Test the creation of a university
def test_create_university(test_db):
    university = create_university(test_db, "Test University")
    assert university.id is not None
    assert university.name == "Test University"

# Test the creation of a survey linked to a university
def test_create_survey(test_db):
    university = create_university(test_db, "Another Test University")
    survey = create_survey(test_db, "New Survey", university.id)
    assert survey.id is not None
    assert survey.title == "New Survey"
    assert survey.university_id == university.id

# Test retrieving surveys for a specific university
def test_get_university_surveys(test_db):
    university = create_university(test_db, "Survey University")
    survey1 = create_survey(test_db, "Survey 1", university.id)
    survey2 = create_survey(test_db, "Survey 2", university.id)

    surveys = test_db.query(Survey).filter(Survey.university_id == university.id).all()
    assert len(surveys) == 2
    assert surveys[0].title == "Survey 1"
    assert surveys[1].title == "Survey 2"

# Additional tests can cover updates and deletions, complex queries, and transaction handling
