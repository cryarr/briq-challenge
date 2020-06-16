from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


##really simple and dirty way to do a rating within flask
## just do a simple html form and on POST then rerun
class rating(FlaskForm):
    rating = StringField('rating', validators=[DataRequired()])
    submit = SubmitField('submit')
