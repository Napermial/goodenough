from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Boolean, Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Grade(Base):
    __tablename__ = "grade"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String)
    category1 = Column(Boolean)
    category2 = Column(Boolean)
    category3 = Column(Boolean)
    category4a = Column(Boolean)
    category4b = Column(Boolean)
    category4c = Column(Boolean)
    category5a = Column(Boolean)
    category5b = Column(Boolean)
    category6a = Column(Boolean)
    category6b = Column(Boolean)
    category7a = Column(Boolean)
    category7b = Column(Boolean)
    category7c = Column(Boolean)
    category7d = Column(Boolean)
    category7e = Column(Boolean)
    category8a = Column(Boolean)
    category8b = Column(Boolean)
    category9a = Column(Boolean)
    category9b = Column(Boolean)
    category9c = Column(Boolean)
    category9d = Column(Boolean)
    category9e = Column(Boolean)
    category10a = Column(Boolean)
    category10b = Column(Boolean)
    category10c = Column(Boolean)
    category10d = Column(Boolean)
    category10e = Column(Boolean)
    category11a = Column(Boolean)
    category11b = Column(Boolean)
    category12a = Column(Boolean)
    category12b = Column(Boolean)
    category12c = Column(Boolean)
    category12d = Column(Boolean)
    category12e = Column(Boolean)
    category13 = Column(Boolean)
    category14a = Column(Boolean)
    category14b = Column(Boolean)
    category14c = Column(Boolean)
    category14d = Column(Boolean)
    category14e = Column(Boolean)
    category14f = Column(Boolean)
    category15a = Column(Boolean)
    category15b = Column(Boolean)
    category16a = Column(Boolean)
    category16b = Column(Boolean)
    category16c = Column(Boolean)
    category16d = Column(Boolean)
    category17a = Column(Boolean)
    category17b = Column(Boolean)
    category18a = Column(Boolean)
    category18b = Column(Boolean)