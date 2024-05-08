"""
from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from typing import List 
from .. import models, schemas, dependencies

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/manage_universities/", response_class=HTMLResponse, response_model=schemas.UniversityDisplay)
async def manage_universities(request: Request, db: Session = Depends(dependencies.get_db)):
    universities = db.query(models.University).all()
    return templates.TemplateResponse("manage_universities.html", {
        "request": request,
        "universities": universities, 
        # "university": university
    })

@router.get("/manage_universities/", response_class=HTMLResponse, response_model=schemas.UniversityDisplay)
async def manage_universities(request: Request, db: Session = Depends(dependencies.get_db)):
    universities = db.query(models.University).all()
    return templates.TemplateResponse("manage_universities.html", {
        "request": request,
        "universities": universities
    })


@router.post("/create_university")
async def create_university_post(name: str = Form(...), db: Session = Depends(dependencies.get_db)):
    new_university = University(name=name)
    db.add(new_university) 
    db.commit()
    return templates.TemplateResponse("create_university.html", {"request": Request, "message": "University created successfully"})


@router.get("/universities", response_class=HTMLResponse) #response_model=list[schemas.UniversityBase])
def read_universities(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    universities = db.query(models.University).offset(skip).limit(limit).all()
    return universities
    #return templates.TemplateResponse("Universities_list.html", {"request": request, "data": universities})
 

# University Management
@router.post("/universities/", response_model=schemas.UniversityDisplay)
def create_university(university: schemas.UniversityCreate, db: Session = Depends(dependencies.get_db)):
    db_university = models.University(name=university.name)
    db.add(db_university)
    db.commit()
    db.refresh(db_university)
    return db_university
    #return templates.TemplateResponse("create_university.html", {"request" : request, "data" : db_university})

@router.patch("/universities/{university_id}/activate", response_model=schemas.UniversityDisplay)
def activate_university(university_id: int, db: Session = Depends(dependencies.get_db)):
    db_university = db.query(models.University).filter(models.University.id == university_id).first()
    if not db_university:
        raise HTTPException(status_code=404, detail="University not found")
    db_university.is_active = True
    db.commit()
    return db_university

@router.patch("/universities/{university_id}/deactivate", response_model=schemas.UniversityDisplay)
def deactivate_university(university_id: int, db: Session = Depends(dependencies.get_db)):
    db_university = db.query(models.University).filter(models.University.id == university_id).first()
    if not db_university:
        raise HTTPException(status_code=404, detail="University not found")
    db_university.is_active = False
    db.commit()
    return db_university
    """

""" 
from fastapi import APIRouter, Depends, HTTPException, Request, Form, Response
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import List
from .. import models, schemas, dependencies

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/universities/manage", response_class=HTMLResponse)
def manage_universities(request: Request, db: Session = Depends(dependencies.get_db)):
    universities = db.query(models.University).all()
    return templates.TemplateResponse("manage_universities.html", {
        "request": request,
        "universities": universities
    })

@router.get("/universities/create", response_class=HTMLResponse)
def create_university_form(request: Request):
    return templates.TemplateResponse("create_university.html", {"request": request})

@router.post("/universities/", response_class=HTMLResponse)
def create_university(request: Request, name: str = Form(...), db: Session = Depends(dependencies.get_db)):
    db_university = models.University(name=name)
    db.add(db_university)
    db.commit()
    return RedirectResponse(url="/universities/manage", status_code=303)

@router.post("/universities/{university_id}/activate", response_class=HTMLResponse)
def activate_university(request: Request, university_id: int, db: Session = Depends(dependencies.get_db)):
    db_university = db.query(models.University).filter(models.University.id == university_id).first()
    if not db_university:
        raise HTTPException(status_code=404, detail="University not found")
    db_university.is_active = True
    db.commit()
    return RedirectResponse(url="/universities/manage", status_code=303)

@router.post("/universities/{university_id}/deactivate", response_class=HTMLResponse)
def deactivate_university(request: Request, university_id: int, db: Session = Depends(dependencies.get_db)):
    db_university = db.query(models.University).filter(models.University.id == university_id).first()
    if not db_university:
        raise HTTPException(status_code=404, detail="University not found")
    db_university.is_active = False
    db.commit()
    return RedirectResponse(url="/universities/manage", status_code=303)
 """




from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from fastapi.templating import Jinja2Templates
from typing import List 
from .. import models, schemas, dependencies

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/manage", response_model=schemas.UniversityDisplay)
async def manage_universities(request: Request, db: Session = Depends(dependencies.get_db)):
    universities = db.query(models.University).all()
    return templates.TemplateResponse("manage_universities.html", {
        "request": request,
        "universities": universities, 
        # "university": university
    })


@router.get("/universities/", response_model=list[schemas.UniversityBase])
def read_universities(skip: int = 0, limit: int = 100, db: Session = Depends(dependencies.get_db)):
    universities = db.query(models.University).offset(skip).limit(limit).all()
    return universities

# University Management
@router.post("/universities/", response_model=schemas.UniversityDisplay)
def create_university(university: schemas.UniversityCreate, db: Session = Depends(dependencies.get_db)):
    db_university = models.University(name=university.name)
    db.add(db_university)
    db.commit()
    db.refresh(db_university)
    return db_university

@router.patch("/universities/{university_id}/activate", response_model=schemas.UniversityDisplay)
def activate_university(university_id: int, db: Session = Depends(dependencies.get_db)):
    db_university = db.query(models.University).filter(models.University.id == university_id).first()
    if not db_university:
        raise HTTPException(status_code=404, detail="University not found")
    db_university.is_active = True
    db.commit()
    return db_university

@router.patch("/universities/{university_id}/deactivate", response_model=schemas.UniversityDisplay)
def deactivate_university(university_id: int, db: Session = Depends(dependencies.get_db)):
    db_university = db.query(models.University).filter(models.University.id == university_id).first()
    if not db_university:
        raise HTTPException(status_code=404, detail="University not found")
    db_university.is_active = False
    db.commit()
    return db_university