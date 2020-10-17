from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.widgets import TextArea


class Post(FlaskForm):
    post = TextAreaField('Post Comment', render_kw={"rows": 5, "cols": 120})
    submit = SubmitField("Post")
