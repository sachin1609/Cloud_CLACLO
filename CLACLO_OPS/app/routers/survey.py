from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from typing import List 
from .. import models, schemas, dependencies

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Survey Management
@router.post("/surveys/", response_model=schemas.SurveyDisplay)
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(dependencies.get_db)):
    db_survey = models.Survey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

@router.post("/survey-reports/", response_model=schemas.SurveyReportDisplay)
def create_survey_report(report: schemas.SurveyReportCreate, db: Session = Depends(dependencies.get_db)):
    db_report = models.SurveyReport(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

@router.get("/survey-reports/{survey_report_id}", response_model=schemas.SurveyReportDisplay)
def get_survey_report(survey_report_id: int, db: Session = Depends(dependencies.get_db)):
    db_report = db.query(models.SurveyReport).filter(models.SurveyReport.id == survey_report_id).first()
    if not db_report:
        raise HTTPException(status_code=404, detail="Survey report not found")
    return db_report

@router.get("/university/{university_id}/survey-reports", response_model=List[schemas.SurveyReportDisplay])
def get_university_survey_reports(university_id: int, db: Session = Depends(dependencies.get_db)):
    db_reports = db.query(models.SurveyReport).join(models.Survey).filter(models.Survey.university_id == university_id).all()
    if not db_reports:
        raise HTTPException(status_code=404, detail="No survey reports found for this university")
    return db_reports


""" 

from fastapi import APIRouter, Depends, HTTPException, Request, Form
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List
from .. import models, schemas, dependencies

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

# Survey Management
@router.get("/surveys/create", response_class=HTMLResponse)
def create_survey_form(request: Request):
    return templates.TemplateResponse("create_survey.html", {"request": request})

@router.post("/surveys/", response_class=HTMLResponse)
def create_survey(request: Request, survey: schemas.SurveyCreate, db: Session = Depends(dependencies.get_db)):
    db_survey = models.Survey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return templates.TemplateResponse("view_survey_report.html", {"request": request, "survey": db_survey})

@router.get("/survey-reports/create", response_class=HTMLResponse)
def create_survey_report_form(request: Request):
    return templates.TemplateResponse("create_survey_report.html", {"request": request})

@router.post("/survey-reports/", response_class=HTMLResponse)
def create_survey_report(request: Request, report: schemas.SurveyReportCreate, db: Session = Depends(dependencies.get_db)):
    db_report = models.SurveyReport(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return templates.TemplateResponse("view_survey_report.html", {"request": request, "report": db_report})

@router.get("/survey-reports/{survey_report_id}", response_class=HTMLResponse)
def get_survey_report(request: Request, survey_report_id: int, db: Session = Depends(dependencies.get_db)):
    db_report = db.query(models.SurveyReport).filter(models.SurveyReport.id == survey_report_id).first()
    if not db_report:
        raise HTTPException(status_code=404, detail="Survey report not found")
    return templates.TemplateResponse("view_survey_report.html", {"request": request, "report": db_report})

@router.get("/university/{university_id}/survey-reports", response_class=HTMLResponse)
def get_university_survey_reports(request: Request, university_id: int, db: Session = Depends(dependencies.get_db)):
    db_reports = db.query(models.SurveyReport).join(models.Survey).filter(models.Survey.university_id == university_id).all()
    if not db_reports:
        raise HTTPException(status_code=404, detail="No survey reports found for this university")
    return templates.TemplateResponse("view_all_survey_reports.html", {"request": request, "reports": db_reports})
 """