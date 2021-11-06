import databases
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, connect_args={'connect_timeout': 100})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)





