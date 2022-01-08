from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, login_user, current_user
from . import db
from .models import Goals

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == "POST":
        goal = request.form.get("goal")

        if len(goal) > 0 and len(goal) < 80:
            new_goal = Goals(goal=goal, user_id=current_user.id)
            db.session.add(new_goal)
            db.session.commit()
            flash('Goal created!', category = 'success')
        else:
            flash('Goal cannot be empty', category = 'error')
    return render_template("home.html", user=current_user)

@views.route('/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    query_user = User.query.filter_by(username=username).first()
    if request.method == "POST":
        new_follow = Follows(source_id=current_user.id, target_id=query_user.id)
        db.session.add(new_follow)
        db.session.commit()
        flash('Account followed', category = 'success')
    return render_template("user.html", query_user=query_user, user=current_user)
