import email
from sqlalchemy.orm import Session

from ..models import HelloWorldModel
from ..schemas import HelloWorldSchema

class HelloWorldRepository():
    def get_hello_world(db:Session, user_id: int):
        return db.query(HelloWorldModel.HelloWorld).filter(HelloWorldModel.HelloWorld.id==user_id).first()

    def get_hello_world_by_email(db:Session):
        return db.query(HelloWorldModel.HelloWorld).filter(HelloWorldModel.HelloWorld.email==email).first()

    def get_hello_worlds(db:Session, skip: int = 0, limit = 100):
        return db.query(HelloWorldModel.HelloWorld).offset(skip).limit(limit).all()


    def create_hello_world(db: Session, hello_world = HelloWorldSchema.HelloWorldCreate):
        fake_hashed_password = hello_world.password + "notreallyhashed"
        db_hw = HelloWorldModel.HelloWorld(email=hello_world.email, hashed_password=fake_hashed_password)
        db.add(db_hw)
        db.commit()
        db.refresh(db_hw)
        return db_hw