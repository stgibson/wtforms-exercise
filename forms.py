from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import URL, Optional, NumberRange

class AddPetForm(FlaskForm):
    """
        Defines a form to add a pet
    """    
    name = StringField("Name")
    
    species = SelectField("Species", \
        choices=[("cat", "cat"), ("dog", "dog"), ("porcupine", "porcupine")])

    photo_url = StringField("Photo", validators=[URL(), Optional()])

    age = IntegerField("Age", validators=[NumberRange(0, 30), Optional()])

    notes = StringField("Notes")

class EditPetForm(FlaskForm):
    """
        Defines a form to edit a pet
    """
    photo_url = StringField("Photo", validators=[URL(), Optional()])

    notes = StringField("Notes")

    available = BooleanField("Available")