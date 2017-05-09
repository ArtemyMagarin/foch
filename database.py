from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class News(Base):
    __tablename__ = "users"
    uid = Column(Integer, primary_key = True)
    login = Column(String)
    password = Column(String)
    


from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/foch")
Base.metadata.create_all(bind=engine)
from sqlalchemy.orm import sessionmaker
session = sessionmaker(bind=engine)
s = session()

