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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = db.execute("SELECT id FROM users WHERE username = :username AND password = :password", {'username': username, 'password': password}).fetchone()
        print(user)
        if user is None:
            return render_template("registration.html")
        else:
            return render_template("welcome.html", user=user)
    else:
        return render_template("index.html")


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/registration')
def registration():
    return render_template("registration.html")


if __name__ == "__main__":
    app.run()
