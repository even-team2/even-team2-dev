from fastapi import APIRouter, Depends, status
from schemas.response import UserResponse, UserResponseData, responses
from fastapi.security import HTTPBearer
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from utils.authentication import verify_token
from schemas.response import ApiResponse
from database.session import Session
from database.user import get_user


router = APIRouter()

@router.get("/users/me", response_model=UserResponse, responses=responses)
async def me(access_token=Depends(HTTPBearer())) -> UserResponse:
    payload = verify_token(access_token.credentials)
    if payload:
        with Session.begin() as session:
            user = get_user(session, payload['uuid'])
            if user:
                return UserResponse(
                    success=True,
                    data=UserResponseData(
                        uuid=access_token.credentials,
                        user_id=user.user_id,
                        user_name=user.user_name
                    )
                )
            else:
                return JSONResponse(
                    content=jsonable_encoder(ApiResponse(success=False)),
                    status_code=status.HTTP_401_UNAUTHORIZED)
    else:
        return JSONResponse(
            content=jsonable_encoder(ApiResponse(success=False)),
            status_code=status.HTTP_401_UNAUTHORIZED)
