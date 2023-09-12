from typing import Union

from pymongo import MongoClient
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates= Jinja2Templates(directory="templates")
con=MongoClient("mongodb+srv://sanidhya626:Xn2HuadmG4xgkHir@cluster0.penl3go.mongodb.net/")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
     doc=con.Notes.Notes.find_one({})
     print(doc)
     return templates.TemplateResponse("index.html", {"request": request})


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
      
    return {"item_id": item_id, "q": q}