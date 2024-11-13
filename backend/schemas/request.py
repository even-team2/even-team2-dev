from pydantic import BaseModel


class LoginRequest(BaseModel):
    user_id: str
    user_password: str
