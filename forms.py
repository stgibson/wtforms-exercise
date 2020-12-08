from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import URL, Optional, NumberRange

class PetForm(FlaskForm):
    """
        Defines a form to create or add a pet
    """    
    name = StringField("Name")
    
    species = SelectField("Species", \
        choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")])

    photo_url = StringField("Photo", validators=[URL(), Optional()])

    age = IntegerField("Age", validators=[NumberRange(0, 30), Optional()])

    notes = StringField("Notes")