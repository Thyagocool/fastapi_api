from ..repository import HelloWorldRepository
from sqlalchemy.orm import Session
from ..database.Database import SessionLocal, engine

repository = HelloWorldRepository.HelloWorldRepository


class HelloWorldController:

    def __init__(self):
        self.db = SessionLocal()

    print('xxxxxxxxxxxxxxxxxxxxxx')
    def getHelloWorld(db:Session):
        return repository.get_hello_worlds(db)
        #return {"message":"xxxxxxxxxxx"}