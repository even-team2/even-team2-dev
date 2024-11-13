from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi import Security
from fastapi.security import HTTPBearer 
from starlette.exceptions import HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="/openapi.json", title="this is me")

@app.get("/openapi.json", include_in_schema=False)
async def get_openapi_json():
    return app.openapi()


class LoginRequest(BaseModel):
    user_id: str
    user_password: str


class ApiResponse(BaseModel):
    success: bool

class LoginResponseData(BaseModel):
    access_token: str

class LoginResponse(ApiResponse):
    data: LoginResponseData

class UserResponseData(BaseModel):
    uuid: str
    user_id: str
    user_name: str

class UserResponse(ApiResponse):
    data: UserResponseData

class ErrorResponse(ApiResponse):
    message: str


responses = {
    403: {
        "description": "not logged in",
        "content": {
            "application/json": {
                "example": {
                    "success": "false",
                    "message": "error message"
                    }
                }
            }
        },
    422: {
        "description": "validation error",
        "content": {
            "application/json": {
                "example": {
                    "success": "false",
                    "message": "error message"
                    }
                }
            }
        }
    }


def verify_header(access_token=Security(HTTPBearer())):
    return access_token

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


@app.exception_handler(HTTPException)
async def exception_handler(request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder(ErrorResponse(
            success=False,
            message="fail to process request"))
    )

app.include_router(router)
