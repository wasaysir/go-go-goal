from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default = func.now())
    goals = db.relationship('Goals', backref = "User")

    def __repr__(self):
        return '<User %r>' % self.username

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime, default = func.now())
    goal = db.Column(db.String(80), nullable = False)
    user_assoc = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)
    dates = db.relationship('Date_goals', backref = "Goals")

    def __repr__(self):
        return '<Goals %r>' % self.goal

class Date_goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = func.now())
    goal_accomplished = db.Column(db.Boolean, nullable = True)
    goal_assoc = db.Column(db.Integer, db.ForeignKey('Goals.id'), nullable = False)
