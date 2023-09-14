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
   
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}