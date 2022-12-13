import uuid
from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel

from ..helpers.enums import CategoryTypeEnum


class BudgetBase(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    created_at: Optional[date] = datetime.now().date()


class BudgetCreate(BudgetBase):
    name: str
    description: str
    amount: int


class ShowBudget(BudgetBase):
    id: uuid.UUID
    name: str
    description: Optional[str]
    created_at: date
    amount: int
    category: CategoryTypeEnum
    is_active: bool

    class Config:
        orm_mode = True
