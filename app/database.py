from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#Database connection URL
#SQLALCHEMY_DATABASE_URL = 'postgresql://<username>:<password>@<ip-adress/hostname>/<database_name>'
#"postgresql+psycopg2://username:password@localhost:5432/mydatabase"

SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:***********@localhost:5432/fastapi"


# Create Engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)


#Create Session
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)


#Base class for models
Base = declarative_base()




