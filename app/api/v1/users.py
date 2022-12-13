from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ...db.functions.user import (create_new_user, get_user_by_email,
                                  get_user_by_name)
from ...db.session import get_db
from ...schemas.user import ShowUser, UserCreate

router = APIRouter()


@router.post("/", response_model=ShowUser)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user_email = get_user_by_email(email=user.email, db=db)
    if db_user_email:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user_name = get_user_by_name(username=user.username, db=db)
    if db_user_name:
        raise HTTPException(status_code=400, detail="Username already registered")
    return create_new_user(user=user, db=db)
