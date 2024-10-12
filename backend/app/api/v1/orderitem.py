from fastapi import APIRouter, status

from app.schemas.orderitem.orderitem import OrderItemModel
from app.service.orderitem import OrderItemService

router = APIRouter(prefix="/orderitem", tags=["orderitem"])

@router.post("/", response_model=OrderItemCreateModel, status_code=status.HTTP_201_CREATED)
async def create_product(orderitem: OrderItemModel):
    return await OrderItemService.create(orderitem)