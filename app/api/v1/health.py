from fastapi import APIRouter, HTTPException, status
from sqlalchemy.exc import OperationalError

from ...db.session import engine

router = APIRouter()


@router.get("/")
def get_health():
    try:
        with engine.connect():
            pass
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={
                "status": "NOTOK",
                "reason": "db-not-available",
                "description": "cannot connect to database",
            },
        )
    else:
        return {'status': 'OK'}
