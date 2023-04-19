from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

import mpt_app.cruds.problem as problem_crud
import mpt_app.schemas.problem as problem_schema
from mpt_app.db import get_db

router = APIRouter()

@router.get("/problems", response_model=list[problem_schema.Problem])
async def get_problems(db: AsyncSession = Depends(get_db)):
    return await problem_crud.get_problems(db)

# @router.put("/problems/{problem_id}", response_model=problem_schema.Problem)