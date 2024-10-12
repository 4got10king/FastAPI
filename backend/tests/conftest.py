import pytest

from config.db import TestDBSettings
from database.db_accessor import DatabaseAccessor
from database.db_metadata import Base
from database.unitofwork import UnitOfWork


@pytest.fixture
async def test_db_accessor():
    db_settings = TestDBSettings()
    db_accessor = DatabaseAccessor(db_settings)
    await db_accessor.run()
    await db_accessor.init_db(Base)
    return db_accessor


@pytest.fixture
def uow_(test_db_accessor):
    uow = UnitOfWork(database_accessor_p=test_db_accessor)
    return uow
