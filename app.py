from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "kubrick"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

debug = DebugToolbarExtension(app)

connect_db(app)

@app.route("/")
def show_home_page():
    """
        Shows the home page of the website, which displays all of the pets in
        the db
        rtype: str
    """
    pets = Pet.query.all()

    return render_template("home.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def show_add_pet_form():
    """
        Shows a form for the user to add a new pet
        rtype: str
    """
    form = PetForm()

    if form.validate_on_submit():
        pass

    return render_template("add-pet.html", form=form)