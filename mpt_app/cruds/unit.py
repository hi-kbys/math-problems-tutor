from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result
from mpt_app.models.unit import Unit
from mpt_app.schemas.unit import UnitCreate, UnitUpdate


async def get_units(
        db: AsyncSession
        ) -> list[Unit] | None:
    """
    Get all units
    """
    result: Result = await db.execute(
        select(
        Unit
        )
    )
    return result.scalars().all()


async def get_unit(
        db: AsyncSession, 
        unit_id: int
        ) -> Unit | None:
    """
    Get a unit by id
    """
    result : Result  = await db.execute(
        select(Unit).filter(Unit.id == unit_id)
    )
    unit : tuple(Unit) | None = result.first()
    return unit[0] if unit[0] is not None else None


async def create_unit(
        db: AsyncSession,
        unit_create: UnitCreate
        ) -> Unit:
    """
    Create a unit
    """
    unit = Unit(**unit_create.dict())
    db.add(unit)
    await db.commit()
    await db.refresh(unit)
    return unit


async def update_unit(
        db: AsyncSession, 
        unit_update: UnitUpdate,
        unit: Unit
        ) -> Unit:
    """
    Update a unit
    """
    unit.title = unit_update.title
    unit.school_year= unit_update.school_year
    db.add(unit)
    await db.commit()
    await db.refresh(unit)
    return unit

async def delete_unit(
        db: AsyncSession, 
        unit: Unit
        ) -> Unit:
    """
    Delete a unit
    """
    await db.delete(unit)
    await db.commit()
    return unit
