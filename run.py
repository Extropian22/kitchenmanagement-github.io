from app import create_app, db
from app.models import User, Ingredient, Recipe, MenuItem, InventoryTransaction

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Ingredient': Ingredient,
        'Recipe': Recipe,
        'MenuItem': MenuItem,
        'InventoryTransaction': InventoryTransaction
    }

if __name__ == '__main__':
    app.run(debug=True)
