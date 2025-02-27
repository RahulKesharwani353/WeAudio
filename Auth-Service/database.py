from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/WeAudio-Auth"

engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session(bind=engine)