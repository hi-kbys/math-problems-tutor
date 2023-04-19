from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from sqlalchemy.engine import Result

import mpt_app.models.problem as problem_model
import mpt_app.schemas.problem as problem_schema

async def get_problems(db: AsyncSession) -> list[tuple(int, str, str, bool)]:
    stmt = select(problem_model.Problem)
    return await db.execute(stmt)