from app.schemas.product.product import ProductModel
from database.unitofwork import IUnitOfWork, UnitOfWork


class ProductService:
    @classmethod
    async def create(cls, model: ProductModel, uow: IUnitOfWork = UnitOfWork()):
        async with uow:
            return await uow.add_one(model)