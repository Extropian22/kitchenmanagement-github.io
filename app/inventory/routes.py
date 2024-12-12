from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from app import db
from app.inventory import bp
from app.models import Ingredient, InventoryTransaction

@bp.route('/inventory')
@login_required
def index():
    ingredients = Ingredient.query.all()
    return render_template('inventory/index.html', ingredients=ingredients)

@bp.route('/inventory/<int:id>')
@login_required
def view(id):
    ingredient = Ingredient.query.get_or_404(id)
    transactions = InventoryTransaction.query.filter_by(ingredient_id=id).order_by(InventoryTransaction.transaction_date.desc()).all()
    return render_template('inventory/view.html', ingredient=ingredient, transactions=transactions)
