""" 
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .routers import university, survey
from .database import engine
from . import models

# Importing routers
# Assuming you have separate router files under the routers directory for universities and surveys
from .routers.university import router as university_router
from .routers.survey import router as survey_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="University and Survey Management API", version="1.0", description="API for managing universities and conducting surveys")

templates = Jinja2Templates(directory="app/templates")
 
# Include routers
app.include_router(university_router, prefix="/universities", tags=["Universities"])
app.include_router(survey_router, prefix="/surveys", tags=["Surveys"])

# Example of a root endpoint
@app.get("/", tags=["Root"])
async def root():
    # return {"message": "Welcome to the University and Survey Management API!"}
    return templates.TemplateResponse("base.html", {"request": request}) """


from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .routers import university, survey
from .database import engine
from . import models

app = FastAPI(title="University and Survey Management API", version="1.0", description="API for managing universities and conducting surveys")

templates = Jinja2Templates(directory="app/templates")

# Importing routers
from .routers.university import router as university_router
from .routers.survey import router as survey_router

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(university_router, prefix="/universities", tags=["Universities"])
app.include_router(survey_router, prefix="/surveys", tags=["Surveys"])

@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def root(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})
