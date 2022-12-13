import json

from fastapi import APIRouter, HTTPException, status

from ...helpers.config import settings

router = APIRouter()


@router.get("/")
def get_version():
    version = settings.APP_VERSION
    app_name = settings.APP_NAME

    version_dict = {
        "product": app_name,
        "version": version
    }

    try:
        with open("version.json") as json_file:
            data = json.load(json_file)
            version_dict.update(data)
            return version_dict
    except IOError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"description": "Failed to open JSON version file"}
        )
    except TypeError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"description": "Failed to decode JSON version file"},
        )
