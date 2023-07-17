from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result
from mpt_app.models.chapter import Chapter
from mpt_app.schemas.chapter import ChapterCreate, ChapterUpdate


async def get_chapters(
        db: AsyncSession
        ) -> list[Chapter] | None:
    """
    Get all chapters
    """
    result: Result = await db.execute(
        select(
        Chapter
        )
    )
    return result.scalars().all()


async def get_chapter(
        db: AsyncSession, 
        chapter_id: int
        ) -> Chapter | None:
    """
    Get a chapter by id
    """
    result : Result  = await db.execute(
        select(Chapter).filter(Chapter.id == chapter_id)
    )
    chapter : tuple(Chapter) | None = result.first()
    return chapter[0] if chapter[0] is not None else None


async def create_chapter(
        db: AsyncSession,
        chapter_create: ChapterCreate
        ) -> Chapter:
    """
    Create a chapter
    """
    chapter = Chapter(**chapter_create.dict())
    db.add(chapter)
    await db.commit()
    await db.refresh(chapter)
    return chapter


async def update_chapter(
        db: AsyncSession, 
        chapter_update: ChapterUpdate,
        chapter: Chapter
        ) -> Chapter:
    """
    Update a chapter
    """
    chapter.title = chapter_update.title
    chapter.school_year= chapter_update.school_year
    db.add(chapter)
    await db.commit()
    await db.refresh(chapter)
    return chapter

async def delete_chapter(
        db: AsyncSession, 
        chapter: Chapter
        ) -> Chapter:
    """
    Delete a chapter
    """
    await db.delete(chapter)
    await db.commit()
    return chapter
