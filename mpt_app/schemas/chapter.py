from pydantic import BaseModel, Field

class ChapterBase(BaseModel):
    title: str = Field(None, example="場合の数", description="Title of the problem")
    school_year : int = Field(None, example= 1, description="School year of the problem")

class Chapter(ChapterBase):
    id : int

    class Config:
        orm_mode = True

class ChapterCreate(ChapterBase):
    pass

class ChapterCreateResponse(ChapterBase):
    id: int

    class Config:
        orm_mode = True

class ChapterUpdate(ChapterBase):
    pass