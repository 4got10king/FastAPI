from pydantic import condecimal, conint
from app.schemas.base import MyBaseModel


class ProductModel(MyBaseModel):
    name: str
    description: str | None = None
    price: condecimal(ge=0)
    count: conint(ge=0)


class ProductResponseModel(MyBaseModel):
    id: int
    name: str
    description: str | None = None
    price: condecimal(ge=0)
    count: conint(ge=0)
