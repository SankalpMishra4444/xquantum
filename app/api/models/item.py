from pydantic import BaseModel


class ItemBase(BaseModel):
    name: 'abc'


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: 1

    class Config:
        orm_mode = True