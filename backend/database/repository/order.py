from database.models.order import OrderORM
from database.repository.repository import SQLAlchemyRepository


class OrderRepository(SQLAlchemyRepository):
    model = OrderORM