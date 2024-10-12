from pydantic import BaseModel
from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.db_metadata import Base

from app.schemas.orderitem.orderitem import OrderItemResponseModel


class OrderItemORM(Base):
    __tablename__ = "orderitem"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("order.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(Integer, ForeignKey("product.id"), nullable=False)
    count_product: Mapped[int] = mapped_column(Integer)

    order: Mapped["OrderORM"] = relationship("OrderORM", back_populates="order_items")
    product: Mapped["ProductORM"] = relationship("ProductORM")

    def get_schema(self) -> BaseModel:
        return OrderItemResponseModel.from_orm(self)
