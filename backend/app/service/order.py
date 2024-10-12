from typing import List

from fastapi import HTTPException
from app.schemas.order.order import OrderResponseModel
from app.schemas.order.order_status import OrderStatus
from app.schemas.orderitem.orderitem import OrderItemModel, OrderItemResponseModel
from app.service.product import ProductService
from database.unitofwork import IUnitOfWork, UnitOfWork


class OrderService:
    @classmethod
    async def create_order_with_check(
        cls, model: OrderItemModel, uow: IUnitOfWork = UnitOfWork()
    ) -> OrderResponseModel:
        async with uow:
            product = await ProductService.get_by_id(model.product_id)
            if not product or product.count < model.count_product:
                raise HTTPException(status_code=400, detail="Not enough product in stock")

            new_count = product.count - model.count_product
            await ProductService.edit_by_filter(product.id, {"count": new_count})

            return await cls.create(model)

    @classmethod
    async def create(
        cls, model: OrderItemModel, uow: IUnitOfWork = UnitOfWork()
    ) -> OrderItemResponseModel:
        async with uow:
            order = await uow.order.add_one(data={"status": OrderStatus.in_process})
            await uow.order_item.add_one(
                data={
                    "order_id": order.id,
                    "product_id": model.product_id,
                    "count_product": model.count_product,
                }
            )
            await uow.commit()

            res = await uow.order_item.get_by_id(id=order.id)
            return res

    @classmethod
    async def get_all_orders(cls, uow: IUnitOfWork = UnitOfWork()) -> List[OrderResponseModel]:
        async with uow:
            return await uow.order.get_all()

    @classmethod
    async def get_order_by_id(cls, id: int, uow: IUnitOfWork = UnitOfWork()) -> OrderResponseModel:
        async with uow:
            order = await uow.order.get_by_id(id)
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")
            return order

    @classmethod
    async def update_order_status(
        cls, id: int, status: str, uow: IUnitOfWork = UnitOfWork()
    ) -> OrderResponseModel:
        async with uow:
            order = await uow.order.get_by_id(id)
            if not order:
                raise HTTPException(status_code=404, detail="Order not found")

            updated_order = await uow.order.edit_by_filter(
                filters={"id": id}, data={"status": status}
            )
            if not updated_order:
                raise HTTPException(status_code=404, detail="Order not found after update")

            return updated_order
