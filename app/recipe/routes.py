from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from app import db
from app.recipe import bp
from app.models import Recipe

@bp.route('/recipes')
@login_required
def index():
    recipes = Recipe.query.all()
    return render_template('recipe/index.html', recipes=recipes)

@bp.route('/recipe/<int:id>')
@login_required
def view(id):
    recipe = Recipe.query.get_or_404(id)
    return render_template('recipe/view.html', recipe=recipe)
