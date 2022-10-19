from fastapi import FastAPI, Body, Depends, Form, Request
from fastapi.templating import Jinja2Templates

from requests import request
import schemas
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

Base.metadata.create_all(engine)

TEMPLATES = Jinja2Templates(directory="templates")

app = FastAPI()


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get('/')
def read_root():
    return 'hello world'
    # http://127.0.0.1:8000/


@app.get("/table")
#     return 'here is a table'
#     # http://127.0.0.1:8000/table
def getitems(request: Request, db: Session = Depends(get_session)):
    items = db.query(models.Item).all()
    return TEMPLATES.TemplateResponse("new_table.html", {"request": request, "items": items})
 
@app.get("/index")
# http://127.0.0.1:8000/index
# returns Hello world!!! ?
# def index(request: Request):
#     return TEMPLATES.TemplateResponse("index.html", {"request": request})
def getitems(request: Request, db: Session = Depends(get_session)):
    items = db.query(models.Item).all()
    return TEMPLATES.TemplateResponse("index.html", {"request": request, "items": items})
 


# works
# http://127.0.0.1:8000/4


# doesnt' work
# http://127.0.0.1:8000/templates/index.html/

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item

#option #1
# @app.post("/")
# def addItem(task:str):
#     newId = len(fakeDatabase.keys()) + 1
#     fakeDatabase[newId] = {"task":task}
#     return fakeDatabase

#Option #2
@app.post("/")
def addItem(item:schemas.Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)

    return item



@app.put("/{id}")
def updateItem(id:int, item:schemas.Item, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject


@app.delete("/{id}")
def deleteItem(id:int, session: Session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted...'
