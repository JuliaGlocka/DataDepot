from flask import Flask, render_template, request, jsonify
from models import db, Item
from config import Config
import os

app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
    return f"Hello, {username}!"
# Root route for the home page
@app.route('/')
def home():
    return "Welcome to DataDepot!"



# Load configuration from the Config class
app.config.from_object(Config)

# Add the database URI to the app configuration (make sure this is defined in your Config class)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@localhost/{Config.DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional, to disable a feature not used

# Initialize SQLAlchemy
db.init_app(app)

# Creating tables in the database (only in the development setup)
with app.app_context():
    db.create_all()  # You can replace this with migrations in a production environment

# CRUD Endpoints
@app.route('/items', methods=['GET'])
def get_items():
    """
    Get all items from the database.
    """
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "description": item.description, "price": item.price} for item in items])

@app.route('/items', methods=['POST'])
def create_item():
    """
    Create a new item in the database.
    """
    data = request.json
    new_item = Item(name=data['name'], description=data.get('description'), price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item created successfully", "item": {"id": new_item.id, "name": new_item.name}}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    """
    Update an existing item in the database.
    """
    data = request.json
    item = Item.query.get_or_404(item_id)
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    db.session.commit()
    return jsonify({"message": "Item updated successfully"})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """
    Delete an item from the database.
    """
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
