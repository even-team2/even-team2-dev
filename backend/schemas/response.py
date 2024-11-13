from pydantic import BaseModel


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

