import pytest
from app.schemas.order.order_status import OrderStatus
from app.schemas.orderitem.orderitem import OrderItemModel
from app.service.order import OrderService
from database.unitofwork import UnitOfWork


@pytest.mark.asyncio
async def test_create_order_with_check(uow_: UnitOfWork):
    product_data = {"id": 1, "count": 10}
    order_data = OrderItemModel(product_id=1, count_product=5)

    async with uow_:
        await uow_.product.add_one(data=product_data)
        await uow_.commit()

    created_order = await OrderService.create_order_with_check(order_data, uow_)

    assert created_order.product_id == order_data.product_id
    assert created_order.count_product == order_data.count_product

    async with uow_:
        product = await uow_.product.get_by_id(order_data.product_id)
        assert product.count == 5

        await uow_.order.delete_by_id(created_order.id)
        await uow_.commit()


@pytest.mark.asyncio
async def test_create_order(uow_: UnitOfWork):
    product_data = {"id": 1, "count": 10}
    order_data = OrderItemModel(product_id=1, count_product=5)

    async with uow_:
        await uow_.product.add_one(data=product_data)
        await uow_.commit()

    created_order = await OrderService.create(order_data, uow_)

    assert created_order.product_id == order_data.product_id
    assert created_order.count_product == order_data.count_product

    async with uow_:
        await uow_.order.delete_by_id(created_order.id)
        await uow_.commit()


@pytest.mark.asyncio
async def test_get_all_orders(uow_: UnitOfWork):
    product_data = {"id": 1, "count": 10}
    order_data = OrderItemModel(product_id=1, count_product=5)

    async with uow_:
        await uow_.product.add_one(data=product_data)
        await uow_.commit()

    await OrderService.create_order_with_check(order_data, uow_)
    orders = await OrderService.get_all_orders(uow_)

    assert len(orders) > 0

    async with uow_:
        await uow_.order.delete_by_id(orders[0].id)
        await uow_.commit()


@pytest.mark.asyncio
async def test_get_order_by_id(uow_: UnitOfWork):
    product_data = {"id": 1, "count": 10}
    order_data = OrderItemModel(product_id=1, count_product=5)

    async with uow_:
        await uow_.product.add_one(data=product_data)
        await uow_.commit()

    created_order = await OrderService.create_order_with_check(order_data, uow_)
    fetched_order = await OrderService.get_order_by_id(created_order.id, uow_)

    assert fetched_order.id == created_order.id

    async with uow_:
        await uow_.order.delete_by_id(created_order.id)
        await uow_.commit()


@pytest.mark.asyncio
async def test_update_order_status(uow_: UnitOfWork):
    product_data = {"id": 1, "count": 10}
    order_data = OrderItemModel(product_id=1, count_product=5)

    async with uow_:
        await uow_.product.add_one(data=product_data)
        await uow_.commit()

    created_order = await OrderService.create_order_with_check(order_data, uow_)
    updated_order = await OrderService.update_order_status(
        created_order.id, OrderStatus.completed, uow_
    )

    assert updated_order.status == OrderStatus.completed

    async with uow_:
        await uow_.order.delete_by_id(created_order.id)
        await uow_.commit()
