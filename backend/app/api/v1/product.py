from fastapi import APIRouter, status

from app.schemas.product.product import ProductModel
from app.service.product import ProductService

router = APIRouter(prefix="/product", tags=["product"])


@router.post("/", response_model=ProductModel, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductModel):
    return await ProductService.create(product)