from database.models.orderitem import OrderItemORM
from database.repository.repository import SQLAlchemyRepository


class OrderItemRepository(SQLAlchemyRepository):
    model = OrderItemORM