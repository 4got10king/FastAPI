from typing import List
from fastapi import APIRouter, HTTPException, status

from app.schemas.product.product import ProductModel, ProductResponseModel
from app.service.product import ProductService

router = APIRouter(prefix="/product", tags=["product"])


@router.post("/", response_model=ProductResponseModel, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductModel):
    created_product = await ProductService.create(product)
    return created_product


@router.get("/", status_code=status.HTTP_200_OK)
async def get_all() -> List[ProductResponseModel]:
    return await ProductService.get_all()


@router.get("/{id}", status_code=status.HTTP_200_OK)
async def get_by_id(id: int) -> ProductModel:
    product = await ProductService.get_by_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.put("/{id}", response_model=ProductResponseModel, status_code=status.HTTP_200_OK)
async def edit_product(id: int, product_data: ProductModel) -> ProductResponseModel:
    product = await ProductService.get_by_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    updated_product = await ProductService.edit_by_filter(id, product_data.model_dump())

    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found after update")

    return updated_product


@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_one(id: int):
    product = await ProductService.get_by_id(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not foucnd")

    await ProductService.delete_by_id(id)
    return status.HTTP_200_OK
