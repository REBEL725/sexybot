import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from userbot.Config import Config

# the secret configuration specific things
from var import Var

DB_URI = os.environ.get("DATABASE_URL", None)


def start() -> scoped_session:
    db_url = (
        Config.DB_URI.replace("postgres://", "postgresql://")
        if "postgres://" in Config.DB_URI
        else Config.DB_URI
    )
    engine = create_engine(Config.DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    print(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    print(str(e))
