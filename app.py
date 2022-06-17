"""Flask app for adopt app."""

from flask import Flask, redirect, render_template, request

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def homepage():
    '''redirect to users list'''

    return redirect('/homepage')

@app.get("/homepage")
def show_homepage():
    '''display pets and status of adoptability'''

    pets = Pet.query.all()
    return render_template("homepage.html", pets=pets)
