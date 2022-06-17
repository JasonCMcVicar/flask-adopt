"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Email


class AddPetForm(FlaskForm):
    """" a form for adding a pet"""

    name = StringField('Pet Name')
    species = StringField('Species')
    photo_url = StringField('Photo URL')
    age = SelectField('Age',
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')]
                      )
    notes = TextAreaField('notes')
