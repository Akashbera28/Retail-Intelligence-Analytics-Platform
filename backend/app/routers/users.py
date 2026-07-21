from fastapi import APIRouter, Depends

from app.auth import get_current_user
from app.models import User
from app.schemas import UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/me",
    response_model=UserResponse,
)
def get_current_user_profile(
    current_user: User = Depends(get_current_user),
):
    """
    Return the currently authenticated user's profile.
    """
    return current_user