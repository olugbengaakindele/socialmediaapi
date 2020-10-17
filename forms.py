from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.widgets import TextArea


class Post(FlaskForm):
    post = TextAreaField('Post Comment', render_kw={"rows": 5, "cols": 120})
    platform = SelectField("Choose a platform", choices=[("Facebook","Facebook"),("Instagram","Instagram")])
    submit = SubmitField("Post")
