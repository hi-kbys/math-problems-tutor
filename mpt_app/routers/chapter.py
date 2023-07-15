from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

import mpt_app.cruds.chapter as chapter_crud
import mpt_app.schemas.chapter as chapter_schema
from mpt_app.db.session import get_db

router = APIRouter()

@router.get("/chapters", response_model=list[chapter_schema.Chapter], 
    summary="Get all chapters"
    )
async def list_chapters(
    db: AsyncSession = Depends(get_db)
    )-> list[chapter_schema.Chapter]:
    return await chapter_crud.get_chapters(db)

@router.get("/chapters/{chapter_id}", response_model=chapter_schema.Chapter)
async def get_chapter(
    chapter_id: int, 
    db: AsyncSession = Depends(get_db)
    )-> chapter_schema.Chapter:
    chapter = await chapter_crud.get_chapter(db, chapter_id)
    if chapter is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")
    return chapter

@router.post("/chapters", response_model=chapter_schema.ChapterCreateResponse)
async def create_chapter(
    chapter_create: chapter_schema.ChapterCreate,
    db: AsyncSession = Depends(get_db)
    )-> chapter_schema.ChapterCreateResponse:
    return await chapter_crud.create_chapter(db, chapter_create)

@router.put("/chapters/{chapter_id}", response_model=chapter_schema.Chapter)
async def update_chapter(
    chapter_id: int,
    chapter_update: chapter_schema.ChapterUpdate,
    db: AsyncSession = Depends(get_db)
    )-> chapter_schema.Chapter:
    chapter = await chapter_crud.get_chapter(db, chapter_id)
    if chapter is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")
    return await chapter_crud.update_chapter(db, chapter_update, chapter)


@router.delete("/chapters/{chapter_id}", response_model=None)
async def delete_chpater(
    chapter_id: int,
    db: AsyncSession = Depends(get_db)
    )-> None:
    chapter = await chapter_crud.get_chapter(db, chapter_id)
    if chapter is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Chapter not found")
    chapter = await chapter_crud.delete_chapter(db, chapter)
    # 一旦Noneを返す
    return None
