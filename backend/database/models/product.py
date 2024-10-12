from pydantic import BaseModel

from app.schemas.product.product import ProductModel
from database.db_metadata import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float

class ProductORM(Base):
    __tablename__ = "product"
    
    
    id: Mapped[int] = mapped_column(Integer, primary_key = True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    price: Mapped[float] = mapped_column(Float)
    count: Mapped[int] = mapped_column(Integer, nullable = False)

    def get_schema(self) -> BaseModel:
        return ProductModel.from_orm(self)