from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from app import db
from app.menu import bp
from app.models import MenuItem, Recipe

@bp.route('/menu')
@login_required
def index():
    menu_items = MenuItem.query.filter_by(is_active=True).all()
    return render_template('menu/index.html', menu_items=menu_items)

@bp.route('/menu/<int:id>')
@login_required
def view(id):
    menu_item = MenuItem.query.get_or_404(id)
    recipe = Recipe.query.get(menu_item.recipe_id) if menu_item.recipe_id else None
    return render_template('menu/view.html', menu_item=menu_item, recipe=recipe)
