import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from ...api.v1.login import get_current_user_from_token
from ...db.functions.budget import (create_new_budget, delete_budget_by_id,
                                    list_budgets, retreive_budget,
                                    update_budget_by_id)
from ...db.models.user import User
from ...db.session import get_db
from ...schemas.budget import BudgetCreate, ShowBudget

router = APIRouter()


@router.post("/", response_model=ShowBudget, status_code=status.HTTP_201_CREATED)
def create_budget(budget: BudgetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    budget = create_new_budget(budget=budget, db=db, owner_id=current_user.id)
    return budget


@router.get("/{id}", response_model=ShowBudget)
def read_budget(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    budget = retreive_budget(id=id, db=db, owner_id=current_user.id)
    if not budget:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Budget with this id {id} does not exist"
        )
    return budget


@router.get("/", response_model=Page[ShowBudget])
def read_budgets(db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    budgets = list_budgets(db=db, owner_id=current_user.id)
    return paginate(budgets)


@router.put("/{id}")
def update_budget(id: uuid.UUID, budget: BudgetCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    message = update_budget_by_id(id=id, budget=budget, db=db, owner_id=current_user.id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Budget with id {id} not found")
    return {"msg": "Successfully updated data"}


@router.delete("/{id}")
def delete_budget(id: uuid.UUID, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    budget = retreive_budget(id=id, db=db, owner_id=current_user.id)
    if not budget:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Budget with {id} does not exist"
        )
    print(budget.owner_id, current_user.id, current_user.is_superuser)
    if budget.owner_id == current_user.id or current_user.is_superuser:
        delete_budget_by_id(id=id, db=db, owner_id=current_user.id)
        return {"msg": "Successfully deleted"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="You are not permitted!!!!"
    )
