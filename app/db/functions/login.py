from sqlalchemy.orm import Session

from ..models.user import User


def get_user(username: str, db: Session):
    user = db.query(User).filter(User.username == username).first()
    return user
