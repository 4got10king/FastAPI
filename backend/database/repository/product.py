from sqlalchemy import select
from app.schemas.product.product import ProductResponseModel
from database.models.product import ProductORM
from database.repository.repository import SQLAlchemyRepository


class ProductRepository(SQLAlchemyRepository):
    model = ProductORM

    async def get_by_name(self, name: str) -> ProductResponseModel:
        stmt = select(self.model).where(self.model.name == name)
        result = await self.session.execute(stmt)
        product = result.scalar_one_or_none()
        return product.get_schema() if product else None
