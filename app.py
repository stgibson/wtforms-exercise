from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "kubrick"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
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
def add_pet():
    """
        Shows a form for the user to add a new pet, and handles adding a pet
        rtype: str
    """
    form = AddPetForm()

    if form.validate_on_submit():
        # retrieve form data
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        # if optional fields are blank, set to None
        if not photo_url:
            photo_url = None
        if not age:
            age = None
        if not notes:
            notes = None
    
        # create new pet
        new_pet = Pet(name=name, species=species, photo_url=photo_url, \
            age=age, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect("/")

    return render_template("add-pet.html", form=form)

@app.route("/<int:pet_id>", methods=["GET", "POST"])
def show_and_edit_pet(pet_id):
    """
        Shows the details of the pet with id pet_id and a form to edit the pet,
        and handles editing a pet
        type pet_id: int
        rtype: str
    """
    # get info on the pet
    pet = Pet.query.get(pet_id)
    
    # if photo is placeholder, remove for display on form
    if pet.photo_url == Pet.placeholder_image:
        pet.photo_url = None

    # create form with info
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        # get form data
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

        # if optional fields are blank, set to None
        if not photo_url:
            photo_url = Pet.placeholder_image
        if not notes:
            notes = None

        # update pet
        pet.photo_url = photo_url
        pet.notes = notes
        pet.available = available
        db.session.add(pet)
        db.session.commit()

        return redirect("/")

    return render_template("display-pet.html", pet=pet, form=form)