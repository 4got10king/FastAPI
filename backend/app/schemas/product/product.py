import datetime
from app.schemas.base import MyBaseModel


class ProductModel(MyBaseModel):
    id: int
    name: str
    description: str | None
    price: float
    count: int
