#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Post

engine = create_engine('postgresql://username:password@localhost/database_name')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Seed data
user1 = User(username="user1")
user2 = User(username="user2")

post1 = Post(title="Post 1", content="Content of Post 1", author=user1)
post2 = Post(title="Post 2", content="Content of Post 2", author=user2)

session.add_all([user1, user2, post1, post2])
session.commit()

session.close()
