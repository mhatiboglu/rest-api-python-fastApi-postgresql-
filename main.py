from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

class Item(BaseModel):
    id: int
    name:str
    country:str
    age:int
    class Config:
        orm_mode = True

app=FastAPI()
db=SessionLocal()

@app.get('/')
def index():
    return {"message" : "Hello World"}

@app.get('/get',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

