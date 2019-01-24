from model import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///users.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_User(username, password):
    user_object = User(name=username,
     password=password)
    session.add(user_object)
    session.commit()

def query_user_by_name(username):
	name = session.query(
		User).filter_by(name=username).first()
	return name

def query_by_name_and_password(username, password):
    return session.query(User).filter_by(name = username, password = password).first()

def delete_all_users():
    session.query(User).delete()
    session.commit()

