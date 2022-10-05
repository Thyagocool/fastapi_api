from pydantic import BaseModel

class HelloWorldBase(BaseModel):
    email: str


class HelloWorldCreate(HelloWorldBase):
    password: str


class HelloWorld(HelloWorldBase):
    id: int
    is_active: bool
#    items: list[Item] = []

    class Config:
        orm_mode = True