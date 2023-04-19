from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from mpt_app.db import get_db
import mpt_app.cruds.problem as problem_crud
import mpt_app.schemas.problem as problem_schema

router = APIRouter()

@router.get("/problems", response_model=list[problem_schema.Problem])
def get_problems(db: Session = Depends(get_db)):
    return problem_crud.get_problems(db)