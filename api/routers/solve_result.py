from typing import List
import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import api.schemas.solve_result as solve_result_schema
import api.cruds.solve_result as solve_result_crud
from api.db import get_db

router = APIRouter()

@router.get("/results", response_model=List[solve_result_schema.SolveResult])
async def list_results():
    return [solve_result_schema.SolveResult(id=1, time=9.321, date=datetime.datetime.now())]

@router.post("/results", response_model=solve_result_schema.SolveResultCreateResponse)
async def create_result(solve_result_body: solve_result_schema.SolveResultCreate, db: AsyncSession = Depends(get_db)):
    return await solve_result_crud.create_result(db, solve_result_body)

@router.put("/results/{result_id}", response_model=solve_result_schema.SolveResultCreateResponse)
async def update_result(result_id: int, solve_result_body: solve_result_schema.SolveResultCreate):
    return solve_result_schema.SolveResultCreateResponse(id=result_id, **solve_result_body.model_dump())

@router.delete("/results/{result_id}", response_model=None)
async def delete_result(result_id: int):
    return
