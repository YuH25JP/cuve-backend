from sqlalchemy.ext.asyncio import AsyncSession

import api.models.solve_result as solve_result_model
import api.schemas.solve_result as solve_result_schema

async def create_result(db: AsyncSession, soleve_result_create: solve_result_schema.SolveResultCreate) -> solve_result_model.SolveResult:
    solve_result = solve_result_model.SolveResult(**soleve_result_create.model_dump())
    db.add(solve_result)
    await db.commit()
    await db.refresh(solve_result)
    return solve_result
