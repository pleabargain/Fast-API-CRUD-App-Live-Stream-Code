from fastapi import FastAPI, Body, Depends, Form, Request
from fastapi.templating import Jinja2Templates

from requests import request
import schemas
import models
import sqlalchemy

from sqlalchemy.orm import Session 
from database import Base, engine, SessionLocal

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
    return 'Hello world. Please read the README.md file for more information'
    # http://127.0.0.1:8000/



# test it here
# http://127.0.0.1:8000/table
@app.get("/table")
def getitems(request: Request, db: Session = Depends(get_session)):
    items = db.query(models.Item).all()
    return TEMPLATES.TemplateResponse("new_table.html", {"request": request, "items": items})
 
@app.get("/index")
# http://127.0.0.1:8000/index

def getitems(request: Request, db: Session = Depends(get_session)):
    items = db.query(models.Item).all()
    return TEMPLATES.TemplateResponse("index.html", 
                                {"request": request, 
                                "items": items})
 

@app.post("/add_task.html")
def add_task(request: Request, db: Session = Depends(get_session)):
    task = request.form.get("task")
    item = models.Item(task=task)
    db.add(item)
    db.commit()
    return TEMPLATES.TemplateResponse("add_task.html", {"request": request})

# works
# http://127.0.0.1:8000/4


# doesnt' work
# http://127.0.0.1:8000/templates/index.html/

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item



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
