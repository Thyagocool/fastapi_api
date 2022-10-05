from fastapi import Depends, FastAPI, HTTPException
from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..controller import HelloWorldController
from ..schemas import HelloWorldSchema
from ..models import HelloWorldModel
from ..database.Database import SessionLocal, engine


helloWorldController = HelloWorldController.HelloWorldController

HelloWorldModel.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/test", response_model=list[HelloWorldSchema.HelloWorld], tags=["tests"])
async def read_tests(db: Session = Depends(get_db)):
    return helloWorldController.getHelloWorld(db)