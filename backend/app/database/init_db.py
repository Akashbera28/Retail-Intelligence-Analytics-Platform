from app.database import Base, engine

# Import all models here
from app.models import User


def init_db():
    """
    Create all database tables.
    """
    Base.metadata.create_all(bind=engine)