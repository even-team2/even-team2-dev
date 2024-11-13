from fastapi import APIRouter
from schemas.request import LoginRequest
from schemas.response import LoginResponse, LoginResponseData, ApiResponse, responses
from utils.authentication import verify_header


router = APIRouter()

@router.post("/auth/login", response_model=LoginResponse, responses=responses)
async def login(login_request: LoginRequest) -> LoginResponse:
    return LoginResponse(
        success=True,
        data=LoginResponseData(access_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c")
    )

@router.post("/auth/logout", response_model=ApiResponse, responses=responses, dependencies=[verify_header()])
async def logout() -> ApiResponse:
    return ApiResponse(
        success=True
    )
