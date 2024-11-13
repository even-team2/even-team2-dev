from fastapi import Security
from fastapi.security import HTTPBearer


def verify_header(access_token=Security(HTTPBearer())):
    return access_token
