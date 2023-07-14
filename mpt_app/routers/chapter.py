from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

import mpt_app.cruds.chapter as chapter_crud
import mpt_app.schemas.chapter as chapter_schema
from mpt_app.db.db import get_db

router = APIRouter()

@router.get("/chapters", response_model=list[chapter_schema.Chapter], 
    summary="Get all chapters"
    )
async def list_chapters(
    db: AsyncSession = Depends(get_db)
    )-> list[chapter_schema.Chapter]:
    return await chapter_crud.get_chapters(db)
