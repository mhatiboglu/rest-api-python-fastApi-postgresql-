from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

user=os.environ["POSTGRESQL_USER"]
key=os.environ["POSTGRESQL_PASSWORD"]
host=os.environ["POSTGRESQL_HOST"]
db=os.environ["POSTGRESQL_DB"]

engine=create_engine(f"postgresql://{user}:{key}@{host}/{db}",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)