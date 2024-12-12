from flask import render_template, jsonify, redirect, url_for
from flask_login import login_required, current_user
from app.main import bp
from app.models import Recipe, MenuItem, InventoryTransaction, Ingredient
from app import db
from datetime import datetime, timedelta

@bp.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('landing.html')

@bp.route('/dashboard')
@login_required
def dashboard():
    # Get counts for dashboard
    recipe_count = Recipe.query.count()
    menu_count = MenuItem.query.count()
    inventory_count = InventoryTransaction.query.distinct(InventoryTransaction.ingredient_id).count()
    
    # Get low stock alerts
    low_stock_count = Ingredient.query.filter(
        Ingredient.stock_quantity <= Ingredient.minimum_stock
    ).count()

    return render_template('dashboard.html',
        recipe_count=recipe_count,
        menu_count=menu_count,
        inventory_count=inventory_count,
        daily_sales=0,  # Placeholder for now
        weekly_revenue=0.0,  # Placeholder for now
        low_stock_count=low_stock_count
    )

@bp.route('/features')
def features():
    return render_template('features.html')

@bp.route('/pricing')
def pricing():
    return render_template('pricing.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')

@bp.route('/about')
def about():
    return render_template('about.html')

@bp.route('/privacy')
def privacy():
    return render_template('privacy.html')

@bp.route('/terms')
def terms():
    return render_template('terms.html')

@bp.route('/sitemap')
def sitemap():
    return render_template('sitemap.html')

@bp.route('/recipes')
@login_required
def recipes():
    return render_template('recipes.html')

@bp.route('/inventory')
@login_required
def inventory():
    return render_template('inventory.html')

@bp.route('/menu')
@login_required
def menu():
    return render_template('menu.html')

@bp.route('/reports')
@login_required
def reports():
    return render_template('reports.html')

@bp.route('/api/dashboard/stats')
@login_required
def dashboard_stats():
    recipe_count = Recipe.query.count()
    menu_count = MenuItem.query.count()
    inventory_count = InventoryTransaction.query.distinct(InventoryTransaction.ingredient_id).count()
    daily_sales = MenuItem.query.filter(
        MenuItem.last_sold >= datetime.utcnow().date()
    ).with_entities(MenuItem.price).sum() or 0
    
    return jsonify({
        'recipe_count': recipe_count,
        'menu_count': menu_count,
        'inventory_count': inventory_count,
        'daily_sales': f'${daily_sales:,.2f}'
    })
