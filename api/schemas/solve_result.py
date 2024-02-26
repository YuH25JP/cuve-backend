from typing import Optional
import datetime
from pydantic import BaseModel, Field


class SolveResultBase(BaseModel):
    time: Optional[float] = Field(None)
    scramble: Optional[str] = Field(None, example="U R2 D' B2 U' L2 U2 L2 D F2 B' U F' L2 R D2 U F L2")
    comment: Optional[str] = Field(None, example="skip OLL")
    date: Optional[datetime.datetime] = Field(None, description="The date and time of finishing the solve")


class SolveResult(SolveResultBase):
    id: int

    class Config:
        orm_mode = True

class SolveResultCreate(SolveResultBase):
    pass

class SolveResultCreateResponse(SolveResultCreate):
    id: int

    class Config:
        orm_mode = True
