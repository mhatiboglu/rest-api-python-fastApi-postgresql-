from sqlalchemy.sql.expression import null
from database import Base
from sqlalchemy import String,Boolean,Integer,Column,Text


class Item(Base):
    __tablename__='players'
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    country=Column(String(50))
    age=Column(Integer,nullable=False)

    def __repr__(self):
        return f"<Item name={self.name} age={self.age}>"