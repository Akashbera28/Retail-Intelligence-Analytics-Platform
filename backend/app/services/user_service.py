from sqlalchemy.orm import Session

from app.auth.security import hash_password, verify_password
from app.models import User
from app.schemas import UserCreate


class UserService:
    """
    Service class for user registration and authentication.
    """

    @staticmethod
    def get_user_by_email(
        db: Session,
        email: str,
    ):
        """
        Find a user using their email address.
        """

        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def create_user(
        db: Session,
        user_data: UserCreate,
    ):
        """
        Create a new user.

        Returns None if the email is already registered.
        """

        existing_user = UserService.get_user_by_email(
            db=db,
            email=user_data.email,
        )

        if existing_user:
            return None

        new_user = User(
            full_name=user_data.full_name,
            email=user_data.email,
            password_hash=hash_password(
                user_data.password
            ),
            role="user",
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user

    @staticmethod
    def authenticate_user(
        db: Session,
        email: str,
        password: str,
    ):
        """
        Authenticate a user using email and password.

        Returns the user if authentication succeeds.
        Otherwise, returns None.
        """

        user = UserService.get_user_by_email(
            db=db,
            email=email,
        )

        if user is None:
            return None

        if not verify_password(
            password,
            user.password_hash,
        ):
            return None

        return user