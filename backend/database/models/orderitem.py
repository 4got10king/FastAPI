from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.db_metadata import Base

from app.schemas.orderitem.orderitem import OrderItemModel


class OrderItemORM(Base):
    __tablename__ = "orderitem"
    
    id: Mapped[int] = mapped_column(primary_key = True, nullable = False)
    id_product: Mapped[int] = mapped_column(Integer)
    count_product: Mapped[int] = mapped_column(Integer)

    order: Mapped["OrderORM"] = relationship("OrderORM", back_populates="order_items")

    def get_schema(self):
        return OrderItemModel.from_orm(self)