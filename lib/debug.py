from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Post

engine = create_engine('postgresql://username:password@localhost/database_name')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Query data
users = session.query(User).all()
for user in users:
    print(f'User ID: {user.id}, Username: {user.username}')
    for post in user.posts:
        print(f'  Post ID: {post.id}, Title: {post.title}, Content: {post.content}')

session.close()
