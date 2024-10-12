from typing import List
from app.schemas.base import MyBaseModel
from app.schemas.product.product import ProductModel


class OrderItemModel(MyBaseModel):
    product_id: int
    count_product: int


class OrderItemResponseModel(MyBaseModel):
    id: int
    product_id: int
    count_product: int
    order_id: int
    product: List[ProductModel]
