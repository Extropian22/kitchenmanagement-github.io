from datetime import datetime
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), nullable=False, default='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    unit_price = db.Column(db.Float, nullable=False)
    stock_quantity = db.Column(db.Float, nullable=False)
    minimum_stock = db.Column(db.Float, nullable=False)
    calories_per_unit = db.Column(db.Float)
    protein_per_unit = db.Column(db.Float)
    fat_per_unit = db.Column(db.Float)
    carbs_per_unit = db.Column(db.Float)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    serving_size = db.Column(db.Float, nullable=False)
    preparation_time = db.Column(db.Integer)  # in minutes
    instructions = db.Column(db.Text)
    cost_per_serving = db.Column(db.Float)
    selling_price = db.Column(db.Float)
    category = db.Column(db.String(64))
    ingredients = db.relationship('RecipeIngredient', backref='recipe', lazy=True)

class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    quantity = db.Column(db.Float, nullable=False)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(64))
    is_active = db.Column(db.Boolean, default=True)
    sales_count = db.Column(db.Integer, default=0)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class InventoryTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'), nullable=False)
    transaction_type = db.Column(db.String(20), nullable=False)  # 'in' or 'out'
    quantity = db.Column(db.Float, nullable=False)
    unit_price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)
