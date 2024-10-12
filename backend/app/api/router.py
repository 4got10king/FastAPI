from fastapi import APIRouter

from config.api import settings
from app.api.v1.order import router as order_router
from app.api.v1.orderitem import router as orderitem_router
from app.api.v1.product import router as product_router
router = APIRouter(prefix=settings.APP_PREFIX)


router.include_router(order_router)
router.include_router(orderitem_router)
router.include_router(product_router)