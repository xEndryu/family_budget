import json
import os

from fastapi import APIRouter, HTTPException, status

router = APIRouter()


@router.get("/")
def get_version():
    version = os.environ.get("APP_VERSION")
    app_name = os.environ.get("APP_NAME")

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
