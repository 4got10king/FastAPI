import datetime
from typing import List

from app.schemas.base import MyBaseModel
from app.schemas.orderitem.orderitem import OrderItemModel


class OrderModel(MyBaseModel):
    id: int
    creation_date: datetime.datetime 
    status: str

    order_items: List[OrderItemModel]

class OrderCreateModel():
    creation_date: datetime
    status: str
