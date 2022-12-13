from sqlalchemy.orm import Session

from ...helpers.hashing import Hasher
from ...schemas.user import UserCreate
from ..models.user import User


def create_new_user(user: UserCreate, db: Session):
    user = User(
        username=user.username,
        email=user.email,
        hashed_password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_user_by_name(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user
