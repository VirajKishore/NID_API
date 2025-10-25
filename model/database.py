from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQL_ALCHEMY_DATABASE_URL = "sqlite:///./nid.db"

engine = create_engine(SQL_ALCHEMY_DATABASE_URL, echo=True)
DBSession = sessionmaker(engine, autoflush=False)