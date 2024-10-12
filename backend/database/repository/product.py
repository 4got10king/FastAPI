from database.models.product import ProductORM
from database.repository.repository import SQLAlchemyRepository


class ProductRepository(SQLAlchemyRepository):
    model = ProductORM