from typing import Union

from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import FileResponse
from starlette.responses import FileResponse



import db

app = FastAPI()

origins = [
    "http://localhost:8080",
    # "http://127.0.0.1:8000",
    "*",
    # add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None
    
class ItemDay(BaseModel):
    day: str
    key: str

class check(BaseModel):
    key: str

class ItemAddLessons(BaseModel):
    name: str
    price: float
    TeacherId: str
    RoomColor: str
    key: str

class ItemAddSchedule(BaseModel):
    ScheduleDate: str
    LessonId: str
    StudentId: str
    key: str
    
class ItemUpdateSchedule(BaseModel):
   id: str
   key: str

class ItemAddTeachers(BaseModel):
    FirstName: str
    LastName: str
    SalaryPerHour: float
    id: str
    address: str
    password: str
    username: str
    key: str
    permission: str

class ItemAddStudents(BaseModel):
    FirstName: str
    LastName: str
    id: str
    address: str
    key: str

class ItemReport(BaseModel):
    key: str
    month: str
    year: str

class ItemLogin(BaseModel):
    username: str
    password: str
class ItemInfoDay(BaseModel):
    key: str
    day: str


@app.get("/")
def read_root():
    return FileResponse('template/index.html')
@app.get("/login")
def read_root():
    return FileResponse('template/login.html')

@app.get("/src/{filename}")
def read_root(filename: str):
    return FileResponse('template/src/' + filename)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/info/students/")
async def read_item():
    get = await db.studentInfo()
    return {"res":get}

@app.get("/info/teachers/")
async def read_item():
    get = await db.teachersInfo()
    return {"res":get}

@app.get("/info/lessons/")
async def read_item():
    get = await db.lessonsInfo()
    return {"res":get}

@app.post("/info/day/")
async def create_item(item: ItemInfoDay):
    check = await db.token(item.key)
    if check["s"] == 1:
        if check["permission"] > 0: 
            get = await db.get_schedule_day(item.day)
            return {"res":get}
        else:
            return {"res":"you dont have a permission for this"}
    else:
        return {"res":"need to refresh token"}

@app.post("/check")
async def create_item(item: check):
    check = await db.token(item.key)
    return {"res":check}

@app.post("/login")
async def create_item(item: ItemLogin):
  adding = await db.login(item.username,item.password)
  return {"res":adding}

@app.post("/add/lessons")
async def create_item(item: ItemAddLessons):
  check = await db.token(item.key)

  if check["s"] == 1:
    if check["permission"] > 1: 
        adding = await db.newLessons(item.name,item.price,item.TeacherId,item.RoomColor)
        return {"res":adding}
    else:
       return {"res":"you dont have a permission for this"}
  else:
     return {"res":"need to refresh token"}
  

@app.post("/add/teachers")
async def create_item(item: ItemAddTeachers):
  check = await db.token(item.key)

  if check["s"] == 1:
    # if check["permission"] > 1: 
        adding = await db.newTeacher(item.FirstName,item.LastName,item.SalaryPerHour,item.id,item.address,item.username,item.password,item.permission)
        return {"res":adding}
    # else:
    #    return "you dont have a permission for this"
  else:
     return {"res":"need to refresh token"}
  

@app.post("/report")
async def create_item(item: ItemReport):
  check = await db.token(item.key)

  if check["s"] == 1:
    if check["permission"] > 1: 
        adding = await db.report(item.month,item.year)
        return {"res":adding}
    else:
       return {"res":"you dont have a permission for this"}
  else:
     return {"res":"need to refresh token"}
  
@app.post("/add/schedule")
async def create_item(item: ItemAddSchedule):
  check = await db.token(item.key)

  if check["s"] == 1:
    if check["permission"] > 0: 
        adding = await db.newSchedule(item.LessonId,item.StudentId,item.ScheduleDate)
        return {"res":adding}
    else:
       return {"res":"you dont have a permission for this"}
  else:
     return {"res":"need to refresh token"}
  

@app.post("/update/schedule")
async def create_item(item: ItemUpdateSchedule):
  check = await db.token(item.key)

  if check["s"] == 1:
    if check["permission"] > 0: 
        adding = await db.updateSchedule(item.id)
        return {"res":adding}
    else:
        return {"res":"you dont have a permission for this"}
  else:
     return {"res":"need to refresh token"}

@app.post("/add/students")
async def create_item(item: ItemAddStudents):
  
  check = await db.token(item.key)

  if check["s"] == 1:
    if check["permission"] > 0: 
        adding = await db.newStudent(item.FirstName,item.LastName,item.id,item.address)
        return {"res":adding}
    else:
        return {"res":"you dont have a permission for this"}
  else:
     return {"res":"need to refresh token"}
  

@app.delete("/delete/schedule/{id}")
async def delete_hero(id: int):
    delete = await db.delSchedule(id)
    return {"res":delete}


