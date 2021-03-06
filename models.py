from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """
        Defines the schema for the pets table. Includes an id, the pet's name,
        its species, a photo id, its age, any additional notes on the pet, and
        whether or not it is available.
    """
    __tablename__ = "pets"

    placeholder_image = "/static/placeholder.png"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    species = db.Column(db.Text, nullable=False)

    photo_url = db.Column(db.Text, default=placeholder_image)

    age = db.Column(db.Integer)

    notes = db.Column(db.Text)

    available = db.Column(db.Boolean, default=True)