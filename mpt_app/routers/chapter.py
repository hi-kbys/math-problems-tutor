from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

import mpt_app.cruds.unit as unit_crud
import mpt_app.schemas.unit as unit_schema
from mpt_app.db.session import get_db

router = APIRouter()

@router.get("/units", response_model=list[unit_schema.Unit], 
    summary="Get all units"
    )
async def list_units(
    db: AsyncSession = Depends(get_db)
    )-> list[unit_schema.Unit]:
    return await unit_crud.get_units(db)

@router.get("/units/{unit_id}", response_model=unit_schema.Unit)
async def get_unit(
    unit_id: int, 
    db: AsyncSession = Depends(get_db)
    )-> unit_schema.Unit:
    unit = await unit_crud.get_unit(db, unit_id)
    if unit is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unit not found")
    return unit

@router.post("/units", response_model=unit_schema.UnitCreateResponse)
async def create_unit(
    unit_create: unit_schema.UnitCreate,
    db: AsyncSession = Depends(get_db)
    )-> unit_schema.UnitCreateResponse:
    return await unit_crud.create_unit(db, unit_create)

@router.put("/units/{unit_id}", response_model=unit_schema.Unit)
async def update_unit(
    unit_id: int,
    unit_update: unit_schema.UnitUpdate,
    db: AsyncSession = Depends(get_db)
    )-> unit_schema.Unit:
    unit = await unit_crud.get_unit(db, unit_id)
    if unit is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unit not found")
    return await unit_crud.update_unit(db, unit_update, unit)


@router.delete("/units/{unit_id}", response_model=None)
async def delete_chpater(
    unit_id: int,
    db: AsyncSession = Depends(get_db)
    )-> None:
    unit = await unit_crud.get_unit(db, unit_id)
    if unit is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Unit not found")
    unit = await unit_crud.delete_unit(db, unit)
    # 一旦Noneを返す
    return None
