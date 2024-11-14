from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from database.session import Session
from schemas.request import LoginRequest
from schemas.response import LoginResponse, LoginResponseData, ApiResponse, responses
from fastapi.security import HTTPBearer
from utils.authentication import issue_token, verify_token, verify_password, revoke_token
from database.auth import get_auth


router = APIRouter()

@router.post("/auth/login", response_model=LoginResponse)
async def login(login_request: LoginRequest) -> LoginResponse:
    with Session.begin() as session:
        auth = get_auth(session, login_request.user_id)
        if auth != None and verify_password(login_request.user_password, auth.user_password):
            token = issue_token(auth.uuid)

            return LoginResponse(
                success=True,
                data=LoginResponseData(access_token=token)
            )
        else:
            return JSONResponse(
                content=jsonable_encoder(ApiResponse(success=False)), 
                status_code=status.HTTP_401_UNAUTHORIZED)

@router.post("/auth/logout", response_model=ApiResponse, responses=responses)
async def logout(access_token=Depends(HTTPBearer())) -> ApiResponse:
    if verify_token(access_token.credentials):
        revoke_token(access_token.credentials)

        return ApiResponse(
            success=True
        )
    else:
        return JSONResponse(
            content=jsonable_encoder(ApiResponse(success=False)),
            status_code=status.HTTP_401_UNAUTHORIZED)
