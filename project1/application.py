import os

from flask import Flask, session, render_template, url_for, request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/", methods=['POST'])
def index():
    # perhaps this should be the registration page
    # get username and password from form post
    # search the database for this user
    # if no user then send to registration or login page
    return render_template("index.html")

#@app.route("/template")
#def template():
#    """lists something """
#    something = db.execute("SELECT * FROM a_table").fetchall
 #   return render_template("template.html" something=something)
