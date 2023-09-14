from typing import Union
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates=Jinja2Templates(directory="templates")





@app.get("/", response_class=HTMLResponse)
async def read_static(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
   