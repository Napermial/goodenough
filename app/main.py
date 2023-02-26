from fastapi import FastAPI, Form, Depends
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database import Base, engine, SessionLocal, Grade
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["http://localhost", "127.0.0.1", "http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CategoryInputs(BaseModel):
    image_name:str
    category1: bool
    category2: bool
    category3: bool
    category4a: bool
    category4b: bool
    category4c: bool
    category5a: bool
    category5b: bool
    category6a: bool
    category6b: bool
    category7a: bool
    category7b: bool
    category7c: bool
    category7d: bool
    category7e: bool
    category8a: bool
    category8b: bool
    category9a: bool
    category9b: bool
    category9c: bool
    category9d: bool
    category9e: bool
    category10a: bool
    category10b: bool
    category10c: bool
    category10d: bool
    category10e: bool
    category11a: bool
    category11b: bool
    category12a: bool
    category12b: bool
    category12c: bool
    category12d: bool
    category12e: bool
    category13: bool
    category14a: bool
    category14b: bool
    category14c: bool
    category14d: bool
    category14e: bool
    category14f: bool
    category15a: bool
    category15b: bool
    category16a: bool
    category16b: bool
    category16c: bool
    category16d: bool
    category17a: bool
    category17b: bool
    category18a: bool
    category18b: bool

class CategoryGrade(CategoryInputs):
    id:int

    class Config:
        orm_mode = True

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/grade")
async def grade(data: CategoryInputs, db: Session = Depends(get_db)):
    grade = Grade(**data.dict())
    db.add(grade)
    db.commit()
    return {"message": "Grade created successfully."}