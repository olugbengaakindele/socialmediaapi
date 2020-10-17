from flask import Flask, request, render_template, redirect, url_for, flash
from forms import Post
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(26)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class postComment(db.Model):
    __tablename__ = 'postcomment'

    id = db.Column(db.Integer,primary_key= True)
    username = db.Column(db.String(20), nullable=False)
    platform = db.Column(db.String(100), nullable = False)
    comment = db.Column(db.String(100), nullable=False)

    def __init__(self, username, comment, platform
                 ):
        self.username = username
        self.comment = comment
        self.platform = platform

@app.route("/home")
def home():
    form = Post()
    return render_template("obi.html", title="Home Page", form=form)


@app.route("/post", methods=['GET', 'POST'])
def post():
    form = Post()

    if form.validate_on_submit():
        comment = postComment("Olu", comment=form.post.data, platform= form.platform.data)
        db.session.add(comment)
        db.session.commit()
        flash("your comment has been posted and saved in the database")
        return redirect(url_for('post'))
    return render_template("post.html", title="Post Page", form=form)


@app.route("/read")
def read():
    form = Post()
    comments = postComment.query.all()

    return render_template("read.html", title="Read Page", comments = comments)


@app.route("/update")
def update():
    form = Post()
    return render_template("update.html", title="Update Page", form=form)


@app.route("/delete")
def delete():
    form = Post()
    return render_template("delete.html", title="Delete Page", form=form)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
