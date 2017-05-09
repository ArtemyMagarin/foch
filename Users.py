import hashlib
import random
import string
import re

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Users(Base):
    __tablename__ = "Users"
    uid = Column(Integer, primary_key = True)
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    confirmed = Column(Boolean)



class User:

    def __init__(self):

        

        engine = create_engine("mysql+pymysql://root:@127.0.0.1:3306/foch")
        Base.metadata.create_all(bind=engine)
        session = sessionmaker(bind=engine)

        self.s = session()

    def new_user(self, username, email, password):
        
        self.set_username(username)
        self.set_email(email)
        self.set_password(password)
 
        q = Users(username=self.username,
            email=self.email,
            password=self.password,
            confirmed=False)
        self.s.add(q)
        self.s.commit()
        
    def set_username(self, username):
        q = self.s.query(Users).filter(Users.username == username).first()
        if q == None:
            self.username = username
        else:
            raise ValueError("Invalid username")

    def set_email(self, email):
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
        if not match:
            raise ValueError("Invalid email")
        q = self.s.query(Users).filter(Users.email == email).first()
        if q == None:
            self.email = email
        else:
            raise ValueError("Email already exists")

    def make_salt(self):
        salt = ""
        for i in range(5):
            salt = salt + random.choice(string.ascii_letters)
        return salt

    def validate_password(self, password):
        if not(re.match('[a-zA-Z0-9]', password)): raise ValueError("Invalid passwords lang")
        if not(8 < len(password) < 20): raise ValueError("Invalid passwords length")
        if password.islower() or password.isupper(): raise ValueError("Invalid passwords case")
        if not(re.match('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$', password)): raise ValueError("Invalid passwords contain")
        return True

    def set_password(self, pw, salt=None):
        if self.validate_password(pw):
            if salt == None:
                salt = self.make_salt()
            self.password = hashlib.sha256(pw.encode() + salt.encode()).hexdigest() + "," + salt


    def check_password(self, username, user_password):
        q = self.s.query(Users).filter(Users.username == username).first()
        if q == None:
            return False

        password, salt = q.password.split(',')
        if password == hashlib.sha256(user_password.encode() + salt.encode()).hexdigest():
            return q.uid
        return False

