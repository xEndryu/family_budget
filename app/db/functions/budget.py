from sqlalchemy.orm import Session

from ...schemas.budget import BudgetCreate
from ..models.budget import Budget


def create_new_budget(budget: BudgetCreate, db: Session, owner_id: int):
    budget_object = Budget(**budget.dict(), owner_id=owner_id)
    db.add(budget_object)
    db.commit()
    db.refresh(budget_object)
    return budget_object


def retreive_budget(id: int, db: Session, owner_id: int):
    item = db.query(Budget).filter(Budget.id == id, owner_id == owner_id).first()
    return item


def list_budgets(db: Session, owner_id: int, category: str = None):
    budgets = db.query(Budget).filter(Budget.owner_id == owner_id)
    if category:
        budgets = budgets.filter(Budget.category == category)

    return budgets


def update_budget_by_id(id: int, budget: BudgetCreate, db: Session, owner_id):
    existing_budget = db.query(Budget).filter(Budget.id == id, owner_id == owner_id)
    if not existing_budget.first():
        return 0
    budget.__dict__.update(owner_id=owner_id)
    existing_budget.update(budget.__dict__)
    db.commit()
    return 1


def delete_budget_by_id(id: int, db: Session, owner_id):
    existing_budget = db.query(Budget).filter(Budget.id == id, owner_id == owner_id)
    if not existing_budget.first():
        return 0
    existing_budget.delete(synchronize_session=False)
    db.commit()
    return 1
