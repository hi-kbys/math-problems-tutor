from pydantic import BaseModel, Field

class UnitBase(BaseModel):
    title: str = Field(None, example="場合の数", description="Title of the problem")
    school_year : int = Field(None, example= 1, description="School year of the problem")

class Unit(UnitBase):
    id : int

    class Config:
        orm_mode = True

class UnitCreate(UnitBase):
    pass

class UnitCreateResponse(UnitBase):
    id: int

    class Config:
        orm_mode = True

class UnitUpdate(UnitBase):
    pass