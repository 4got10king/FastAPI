from typing import List, Dict
from app.schemas.product.product import ProductModel, ProductResponseModel
from database.unitofwork import IUnitOfWork, UnitOfWork


class ProductService:
    @classmethod
    async def create(
        cls, model: ProductModel, uow: IUnitOfWork = UnitOfWork()
    ) -> ProductResponseModel:
        async with uow:
            existing_product = await uow.product.get_by_name(model.name)
            if existing_product:
                return existing_product

            res = await uow.product.add_one(data={**model.model_dump()})
            await uow.commit()
            return res

    @classmethod
    async def get_all(cls, uow: IUnitOfWork = UnitOfWork()) -> List[ProductResponseModel]:
        async with uow:
            return await uow.product.get_all()

    @classmethod
    async def get_by_id(cls, id: int, uow: IUnitOfWork = UnitOfWork()) -> ProductModel:
        async with uow:
            return await uow.product.get_by_id(id)

    @classmethod
    async def edit_by_filter(
        cls, id: int, data: Dict[str, any], uow: IUnitOfWork = UnitOfWork()
    ) -> ProductResponseModel | None:
        async with uow:
            updated_id = await uow.product.edit_by_filter(filters={"id": id}, data=data)
            if updated_id:
                updated_product = await uow.product.get_by_id(updated_id)
                return updated_product.get_schema() if updated_product else None
            return None

    @classmethod
    async def delete_by_id(cls, id: int, uow: IUnitOfWork = UnitOfWork()):
        async with uow:
            await uow.product.delete_by_id(id=id)
