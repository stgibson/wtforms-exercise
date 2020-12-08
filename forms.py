from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField

class PetForm(FlaskForm):
    """
        Defines a form to create or add a pet
    """
    name = StringField("Name")
    
    species = StringField("Species")

    photo_url = StringField("Photo")

    age = IntegerField("Age")

    notes = StringField("Notes")