import datetime

from app.schemas.base import MyBaseModel
from app.schemas.order.order_status import OrderStatus


class OrderResponseModel(MyBaseModel):
    id: int
    creation_date: datetime.datetime
    status: OrderStatus
