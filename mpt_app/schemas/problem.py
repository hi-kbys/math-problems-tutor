from pydantic import BaseModel, Field

class ProblemBase(BaseModel):
    title: str = Field(None, example="場合の数", description="Title of the problem")
    statement: str = Field(None, example= "N個の物があります。...", description="Statement of the problem")

class ProblemCreate(ProblemBase):
    pass

class ProblemCreateResponse(ProblemBase):
    id: int

    class Config:
        orm_mode = True

class Problem(ProblemBase):
    id : int
    is_solved: bool = Field(False, 
                            description="Whether the problem is solved or not")