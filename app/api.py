"""
Driver code for running FastAPI app. Contains pre-configured sample FastAPI app.
"""
from fastapi import (
    FastAPI,
    APIRouter,
    File,
    UploadFile,
    Query,
    Body,
    Path,
    Depends,
    HTTPException,
)
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, RedirectResponse
import uvicorn
from .routers import users, items
from datetime import datetime
import os
from .database import SessionLocal, engine, get_db
from . import crud, models, schemas
from sqlalchemy.orm import Session

# BASE PATH
BASE_DIR = os.path.dirname(__file__)

models.Base.metadata.create_all(bind=engine)


# FastAPI Config
link = "https://github.com/angel-badillo-hernandez"
title: str = "Title"
description: str = f"""
<a href="/"><img href="/" src="/logo.svg" height=256px></a>
## Welcome to the API!
Brief overview here...
Template created by [Angel Badillo Hernandez](https://github.com/angel-badillo-hernandez)!
Check out my other projects on my [Github](https://github.com/angel-badillo-hernandez)!
<br/>
<br/>
Copyright ©️ {datetime.now().year} Website. All Rights Reserved.
"""
summary: str = (
    "Summary here...."
)
terms_of_service: str = link
version: str = "0.0.1"
contact: dict = {"name": "Name", "url": link, "email": "admin@email.com"}
license_info:dict = {
    "name": "N/A",
    "url": "N/A"
}

app: FastAPI = FastAPI(
    title=title,
    description=description,
    terms_of_service=terms_of_service,
    summary=summary,
    version=version,
    contact=contact,
    # license_info=license_info,
)

# Include API Routers to FastAPI app
app.include_router(users.router)
app.include_router(items.router)


@app.get("/", tags=["/"])
def docs_redirect()-> RedirectResponse:
    """Redirects to the API website homepage.

    Returns:
        RedirectRespose: Redirect response to index.html.
    """
    return RedirectResponse(url="/index.html")


# Mount static files directory
app.mount(
    "/",
    StaticFiles(directory=os.path.join(BASE_DIR, "public"), html=True),
    name="public",
)
