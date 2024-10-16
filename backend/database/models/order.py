from app.schemas.order.order import OrderResponseModel
from app.schemas.order.order_status import OrderStatus
from database.db_metadata import Base
from database.models.mixin import CreationDateMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer

from database.models.orderitem import OrderItemORM


class OrderORM(Base, CreationDateMixin):
    __tablename__ = "order"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    status: Mapped[OrderStatus | None] = mapped_column(default=None)

    order_items: Mapped[list["OrderItemORM"]] = relationship(
        "OrderItemORM", back_populates="order"
    )

    def get_schema(self) -> OrderResponseModel:
        return OrderResponseModel.from_orm(self)
