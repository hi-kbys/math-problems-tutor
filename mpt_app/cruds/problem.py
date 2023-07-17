from typing import Union, Optional
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import mpt_app.models.problem as problem_model
import mpt_app.schemas.problem as problem_schema

import logging

logger = logging.getLogger(__name__)

async def get_problems(
        db: AsyncSession
        ) -> list[problem_model.Problem] | None:
    
    result: Result = await db.execute(select(
        problem_model.Problem.id, 
        problem_model.Problem.title, 
        problem_model.Problem.statement, 
        problem_model.Problem.is_solved
        )
    )

    return result.all()


async def get_problem(
        db: AsyncSession, 
        problem_id: int
        ) -> problem_model.Problem | None:

    result : Result  = await db.execute(
        select(problem_model.Problem).filter(problem_model.Problem.id == problem_id)
    )
    problem : tuple(problem_model.Problem) | None = result.first()

    return problem[0] if problem[0] is not None else None


async def create_problem(
        db: AsyncSession, problem_create: problem_schema.ProblemCreate
        ) -> problem_model.Problem:
    problem = problem_model.Problem(**problem_create.dict())
    db.add(problem)
    await db.commit()
    await db.refresh(problem)
    return problem


async def update_problem(
        db: AsyncSession, 
        problem_update: problem_schema.ProblemUpdate,
        problem: problem_model.Problem
        ) -> problem_model.Problem:
    problem.title = problem_update.title
    problem.statement = problem_update.statement
    problem.is_solved = problem_update.is_solved
    db.add(problem)
    await db.commit()
    await db.refresh(problem)
    return problem


async def delete_problem(
        db: AsyncSession, problem: problem_model.Problem
        ) -> None:
    await db.delete(problem)
    await db.commit()
    