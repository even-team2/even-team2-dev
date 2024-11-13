from fastapi import APIRouter
from schemas.response import UserResponse, UserResponseData, responses
from utils.authentication import verify_header


router = APIRouter()

@router.get("/users/me", response_model=UserResponse, responses=responses, dependencies=[verify_header()])
async def me() -> UserResponse:
    return UserResponse(
        success=True,
        data=UserResponseData(
            uuid="550e8400-e29b-41d4-a716-446655440000",
            user_id="id",
            user_name="name"
        )
    )
