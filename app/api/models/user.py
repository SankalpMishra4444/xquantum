from pydantic import BaseModel


class UserBase(BaseModel):
    username: 'Fast'


class UserCreate(UserBase):
    password: 'abc'


class User(UserBase):
    id: 1

    class Config:
        orm_mode = True