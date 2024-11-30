from flask import Flask, render_template, request, jsonify
from models import db, Item
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Inicjalizacja SQLAlchemy
db.init_app(app)

# Tworzenie tabel w bazie danych
with app.app_context():
    db.create_all()

# Endpointy CRUD
@app.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify([{"id": item.id, "name": item.name, "description": item.description, "price": item.price} for item in items])

@app.route('/items', methods=['POST'])
def create_item():
    data = request.json
    new_item = Item(name=data['name'], description=data.get('description'), price=data['price'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Item created successfully", "item": {"id": new_item.id, "name": new_item.name}}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    item = Item.query.get_or_404(item_id)
    item.name = data.get('name', item.name)
    item.description = data.get('description', item.description)
    item.price = data.get('price', item.price)
    db.session.commit()
    return jsonify({"message": "Item updated successfully"})

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({"message": "Item deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)

