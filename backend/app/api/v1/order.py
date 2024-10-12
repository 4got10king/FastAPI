from fastapi import APIRouter, status

from app.schemas.order.order import OrderCreateModel
from app.service.order import OrderService


router = APIRouter(prefix="/order", tags=["order"])

@router.post("/", response_model=OrderCreateModel, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreateModel):
    return await OrderService.create(order)