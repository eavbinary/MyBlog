from flask import Blueprint, request, render_template
from sqlalchemy.orm import Session

from model.post import Post
from model.tag import Tag
from model.section import Section
from model.user import User

blog_app = Blueprint("blog_app", __name__)


@blog_app.route("/")
def post_list():
    session = Session()
    posts = session.query(Post).all()

    return render_template('list.html', posts=posts)


@blog_app.route("/post/<int:post_id>")
def post_detail(post_id):
    session = Session()
    post = session.query(Post).filter_by(id=post_id).one()

    return render_template('post.html', post=post)


@blog_app.route("/contact/<int:user_id>")
def contact(user_id):
    session = Session()
    user = session.query(User).filter_by(id=user_id).one()
    posts = session.query(Post).filter_by(user_id=user_id).all()

    return render_template('contacts.html', user=user, posts=posts)
