from app.schemas.base import MyBaseModel


class OrderItemModel(MyBaseModel):
    id: int
    id_product: int
    count_product: int

class OrderItemCreate():
    id_product: int
    count_product: int