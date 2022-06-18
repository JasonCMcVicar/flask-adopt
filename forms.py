"""Forms for adopt app."""

from email import message
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Email, EqualTo, AnyOf, URL


class AddPetForm(FlaskForm):
    """" a form for adding a pet"""

    name = StringField('Pet Name',
                        validators=[InputRequired()])
    species = StringField('Species',
                        validators=[InputRequired(), AnyOf(['cat','dog','porcupine'], message='not valid type')])
    photo_url = StringField('Photo_url',
                         validators=[Optional(), URL(require_tld=False, message=None)])
    age = SelectField('Age',
                      choices=[('baby', 'Baby'), ('young', 'Young'),
                               ('adult', 'Adult'), ('senior', 'Senior')]
                      )
    notes = TextAreaField('notes')
