from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


# =====================================
# User Registration Schema
# =====================================
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


# =====================================
# User Login Schema
# =====================================
# Kept for future use (JSON-based login if needed)
class UserLogin(BaseModel):
    email: EmailStr
    password: str


# =====================================
# User Response Schema
# =====================================
class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    role: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


# =====================================
# JWT Access Token Response
# =====================================
class Token(BaseModel):
    access_token: str
    token_type: str


# =====================================
# JWT Token Payload
# =====================================
class TokenData(BaseModel):
    email: str | None = None