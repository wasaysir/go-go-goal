from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
#from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = '}W*bA{4=UglLz&y'
Bootstrap(app)

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, default = datetime.now)
    goals = db.relationship('Goals', backref = "User")

    def __repr__(self):
        return '<User %r>' % self.username

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime, default = datetime.now)
    goal = db.Column(db.String(80), nullable = False)
    user_assoc = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)
    dates = db.relationship('date_goals', backref = "Goals")

    def __repr__(self):
        return '<Goals %r>' % self.goal

class date_goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = datetime.now)
    goal_accomplished = db.Column(db.Boolean, nullable = True)
    goal_assoc = db.Column(db.Integer, db.ForeignKey('Goals.id'), nullable = False)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/<username>/<email>')
def index(username, email):
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()

    return '<h1>Added New user</h1>'

@app.route('/<username>/')
def get_user(username):
    user = User.query.filter_by(username=username).first()

    return f'<h1> The Users email is: { user.email } </h1>'
