from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime, default = func.now())
    goals = db.relationship('Goals')
    following = db.relationship('Follows', foreign_keys="Follows.target_id")
    followers = db.relationship('Follows', foreign_keys="Follows.source_id")

class Goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    start_date = db.Column(db.DateTime, default = func.now())
    goal = db.Column(db.String(80), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    dates = db.relationship('Date_goals')

class Date_goals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime, default = func.now())
    goal_accomplished = db.Column(db.Boolean, nullable = True)
    goals_id = db.Column(db.Integer, db.ForeignKey('goals.id'), nullable = False)

class Follows(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    follow_date = db.Column(db.DateTime, default = func.now())
    source_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    target_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
