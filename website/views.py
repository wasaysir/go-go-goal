from flask import Blueprint, render_template, request, flash, redirect, url_for, session
from flask_login import login_user, login_required, login_user, current_user
from . import db
from .models import Goals, User, Follows, Date_goals
from .form import SearchForm

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

@views.route('/search', methods=['GET', 'POST'])
@login_required
def search_user():
    form = SearchForm(request.form)
    if request.method == "POST":
        return redirect(url_for('.profile', username=form.search.data))
        #return redirect(profile(form.search.data))
    return render_template('search.html', form=form, user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    username_string = request.args['username']
    query_user = User.query.filter_by(username=username_string).first()
    previous_relationship = Follows.query.filter_by(source_id = current_user.id, target_id=query_user.id).first()
    previous_relationship_bool = False
    if previous_relationship:
        previous_relationship_bool = True

    if request.method == "POST":
        if previous_relationship:
            print(previous_relationship.id)
            Follows.query.filter_by(id = previous_relationship.id).delete()
            db.session.commit()
            print("Unfollowed")
        else:
            new_follow = Follows(source_id = current_user.id, target_id=query_user.id)
            db.session.add(new_follow)
            db.session.commit()
            flash('Profile Followed!')

    return render_template('profile.html', user=current_user, query_user=query_user, prev_relationship_bool=previous_relationship_bool)

    query_user = User.query.filter_by(username=username).first()
    if request.method == "POST":
        new_follow = Follows(source_id=current_user.id, target_id=query_user.id)
        db.session.add(new_follow)
        db.session.commit()
        flash('Account followed', category = 'success')
    return render_template("user.html", query_user=query_user, user=current_user)
