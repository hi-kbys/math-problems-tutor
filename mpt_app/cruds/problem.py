from typing import Union
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import mpt_app.models.problem as problem_model
import mpt_app.schemas.problem as problem_schema

async def get_problems(
        db: AsyncSession) -> Union[list[int, str, str, bool], None]:
    result: Result = await db.execute(select(
        problem_model.Problem.id, 
        problem_model.Problem.title, 
        problem_model.Problem.statement, 
        problem_model.Problem.is_solved
        )
    )
    return result.all()

async def create_problems(
        db: AsyncSession, problem_create: problem_schema.ProblemCreate) -> problem_model.Problem:
    problem = problem_model.Problem(**problem_create.dict())
    db.add(problem)
    await db.commit()
    await db.refresh(problem)
    return problem