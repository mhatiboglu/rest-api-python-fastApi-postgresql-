from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine("postgresql://omnicomFifa:omnicom1234@fifa-database-1.c27k5yd9sicz.eu-west-2.rds.amazonaws.com/fifadb",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)