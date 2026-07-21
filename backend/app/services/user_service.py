from sqlalchemy.orm import Session

from app.auth import hash_password, verify_password
from app.models import User
from app.schemas import UserCreate


class UserService:
    @staticmethod
    def get_user_by_email(db: Session, email: str):
        """
        Return a user by email.
        """
        return db.query(User).filter(User.email == email).first()

    @staticmethod
    def create_user(db: Session, user: UserCreate):
        """
        Create a new user.
        """

        existing_user = UserService.get_user_by_email(db, user.email)

        if existing_user:
            return None

        hashed_password = hash_password(user.password)

        new_user = User(
            full_name=user.full_name,
            email=user.email,
            password_hash=hashed_password,
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
        Verify email and password during login.
        """

        user = UserService.get_user_by_email(db, email)

        if user is None:
            return None

        if not verify_password(password, user.password_hash):
            return None

        return user