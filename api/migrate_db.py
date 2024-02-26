from sqlalchemy.ext.asyncio import create_async_engine
import asyncio

from api.models.solve_result import Base

DB_URL = "mysql+aiomysql://root:cuve-dev@db:3306/db?charset=utf8"
engine = create_async_engine(DB_URL, echo=True)

async def reset_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

if __name__ == '__main__':
    asyncio.run(reset_database())
