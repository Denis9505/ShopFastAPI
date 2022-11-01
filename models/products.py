from pydantic import BaseModel


class BaseProduct(BaseModel):
    title: str
    description: str
    price: float
    count: int


class CreateProduct(BaseModel):
    pass
