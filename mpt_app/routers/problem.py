from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

import mpt_app.cruds.problem as problem_crud
import mpt_app.schemas.problem as problem_schema
from mpt_app.db import get_db

router = APIRouter()

@router.get("/problems", response_model=list[problem_schema.Problem], 
    summary="Get all problems"
    )
async def list_problems(
    db: AsyncSession = Depends(get_db)
    )-> list[problem_schema.Problem]:
    return await problem_crud.get_problems(db)


@router.get("/problems/{problem_id}", response_model=problem_schema.Problem)
async def get_problem(
    problem_id: int, 
    db: AsyncSession = Depends(get_db)
    ) -> any:
    problem: problem_schema.Problem = await problem_crud.get_problem(db, problem_id)
    if problem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem not found")
    return problem


@router.post("/problems", response_model=problem_schema.ProblemCreateResponse)
async def create_problem(
    problem: problem_schema.ProblemCreate, 
    db: AsyncSession = Depends(get_db)
    ):
    """
    Create a new problem
    """
    return await problem_crud.create_problem(db, problem)


@router.put("/problems/{problem_id}", response_model=problem_schema.Problem)
async def update_problem(
    problem_id: int, 
    problem_update: problem_schema.ProblemUpdate,
    db: AsyncSession = Depends(get_db)
    ):
    """
    Update a problem
    """
    problem: problem_schema.Problem = await problem_crud.get_problem(db, problem_id)
    if problem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem not found")
    print(f"problem's id is {problem.id}")
    return await problem_crud.update_problem(db, problem_update, problem)


@router.delete("/problems/{problem_id}", response_model=None)
async def delete_problem(
    problem_id: int, 
    db: AsyncSession = Depends(get_db)
    ) -> None:
    """
    Delete a problem
    """
    problem: problem_schema.Problem = await problem_crud.get_problem(db, problem_id)
    
    if problem is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Problem not found")
    
    return await problem_crud.delete_problem(db, problem)