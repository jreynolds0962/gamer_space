from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

db_user = os.environ['DATABASE_USER']
db_password = os.environ['DATABASE_PASSWORD']
database = os.environ['DATABASE_NAME']


#Connect to Database
engine = create_engine(
    f"mariadb+mariadbconnector://{db_user}:{db_password}@127.0.0.1:3306/{database}"
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()