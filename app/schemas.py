from pydantic import BaseModel


class User(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    age: int

    class Config:
        orm_mode=True