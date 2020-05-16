import os

from flask import Flask, flash, session, render_template, url_for, request, redirect
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
            return render_template("welcome.html", user=username)
    else:
        users = db.execute("SELECT * FROM users").fetchall()
        for user in users:
            print(user)
        return render_template("index.html")


@app.route('/welcome')
def welcome():
    return render_template("welcome.html")


@app.route('/registration', methods=['GET','POST'])
def registration():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # does the account user already exist?
        user = db.execute("SELECT id FROM users WHERE username = :username AND password = :password", {'username': username, 'password': password}).fetchone()
        # if not then create user and go to welcome page
        if user is None:
            db.execute("INSERT INTO users (username, password) VALUES (:username, :password)", {'username': username, 'password': password})
            db.commit()
            flash('You were successfully registered')
            return redirect(url_for("welcome"))
        # if it does then flash message and return to login page
        else:
            flash('Account already exists')
            return redirect(url_for('index'))

    return render_template("registration.html")


if __name__ == "__main__":
    app.run()
