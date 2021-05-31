from flask import Flask, render_template, redirect
from sqlalchemy.orm import Session

from model.post import Post
from views.blog import blog_app

app = Flask(__name__)
app.register_blueprint(blog_app)

if __name__ == '__main__':
    app.run(host='localhost', port=5050, debug=True)
