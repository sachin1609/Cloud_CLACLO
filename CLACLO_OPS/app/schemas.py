from pydantic import BaseModel
from datetime import date
from typing import Optional, List

class UniversityBase(BaseModel):
    name: str
    is_active: bool = True

class UniversityCreate(UniversityBase):
    pass

class UniversityDisplay(UniversityBase):
    id: int
    activation_date: Optional[date] = None
    deactivation_date: Optional[date] = None
    surveys: List[str] = []  # This might need to be updated based on how you handle surveys data.

    class Config:
        orm_mode = True

class SurveyBase(BaseModel):
    university_id: int
    survey_type: str
    data: str
    conducted_on: date

class SurveyCreate(SurveyBase):
    pass

class SurveyDisplay(SurveyBase):
    id: int
    conducted_on: date

    class Config:
        orm_mode = True

class SurveyReportBase(BaseModel):
    survey_id: int
    detailed_report: str

class SurveyReportCreate(SurveyReportBase):
    pass

class SurveyReportDisplay(SurveyReportBase):
    id: int

    class Config:
        orm_mode = True
