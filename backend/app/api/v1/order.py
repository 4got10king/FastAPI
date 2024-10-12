from fastapi import APIRouter, status, HTTPException

from app.schemas.order.order import OrderResponseModel
from app.schemas.order.order_status import OrderStatus
from app.schemas.orderitem.orderitem import OrderItemModel
from app.service.order import OrderService


router = APIRouter(prefix="/order", tags=["order"])


@router.post("/", response_model=OrderItemModel, status_code=status.HTTP_201_CREATED)
async def create(order: OrderItemModel) -> OrderResponseModel:
    created_order = await OrderService.create_order_with_check(order)
    return created_order


@router.get("/", response_model=list[OrderResponseModel], status_code=status.HTTP_200_OK)
async def get_orders() -> list[OrderResponseModel]:
    orders = await OrderService.get_all_orders()
    return orders


@router.get("/{id}", response_model=OrderResponseModel, status_code=status.HTTP_200_OK)
async def get_order(id: int) -> OrderResponseModel:
    order = await OrderService.get_order_by_id(id)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Order not found")
    return order


@router.patch("/{id}/status", response_model=OrderResponseModel, status_code=status.HTTP_200_OK)
async def update_order_status(id: int, status: OrderStatus) -> OrderResponseModel:
    updated_order = await OrderService.update_order_status(id, status.value)
    return updated_order
