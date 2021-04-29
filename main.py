import json

from sqlalchemy.orm import Session, joinedload
from base import Base, DB_NAME
import os.path as path
import os

from user import User
from section import Section
from post import Post
from tag import Tag


def init_db():
    session = Session()

    file = open('example.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()

    for user in data['Users']:
        item = User(username=user['username'])
        session.add(item)

    for section in data['Sections']:
        item = Section(title=section['title'])
        session.add(item)

    for post in data['Posts']:
        item = Post(title=post['title'],
                    section_id=post['section_id'],
                    user_id=post['user_id'],
                    description=post['description'])
        session.add(item)

    for tag in data['Tags']:
        item = Tag(name=tag['name'],
                   post_id=tag['post_id'])
        session.add(item)
    session.commit()
    session.close()


if __name__ == '__main__':
    if path.exists(DB_NAME):
        os.remove(DB_NAME)

    Base.metadata.create_all()
    init_db()

    session = Session()
    user = session.query(User).filter_by(id=1).one()
    print(f'1. Пользователь с ID=1: {user}')

    result = session.query(Post).\
        join(User, User.id == Post.user_id).\
        where(User.username == 'Матвей').all()
    print(f"2. Все посты от Матвея: {result}")

    result = session.query(Section).\
        join(Post, Section.id == Post.section_id).\
        group_by(Section.id).\
        filter(Post.description.like('%Красиво%')).all()
    print(f"3. Все группы где в содержании поста есть слово Красиво: {result}")

    result = session.query(Post).\
        join(Tag,Tag.post_id == Post.id).\
        join(User, User.id == Post.user_id).\
        where((Tag.name == 'природа' or Tag.name == 'крым') and User.username == 'Матвей').all()
    print(f'4. Все посты Матвея тегу Природа или Крым: {result}')
    session.close()
