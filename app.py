from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

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