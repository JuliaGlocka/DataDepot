from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{Config.DB_USER}:{Config.DB_PASSWORD}@localhost/{Config.DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the database model
class DataDepot(db.Model):
    __tablename__ = 'datadepot_db'
    id = db.Column(db.Integer, primary_key=True)  # SERIAL PRIMARY KEY
    name = db.Column(db.String(255))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(255))
    country = db.Column(db.String(100))
    region = db.Column(db.String(50))
    list = db.Column(db.String(255))
    alphanumeric = db.Column(db.String(255))
    currency = db.Column(db.String(100))
    numberrange = db.Column(db.Integer)
    text = db.Column(db.Text)
    postalZip = db.Column(db.String(10))
    address = db.Column(db.String(255))

# Create tables in the database (only for development)
with app.app_context():
    db.create_all()

# Root route
@app.route('/')
def home():
    return "Welcome to DataDepot!"

# CRUD Endpoints
@app.route('/records', methods=['GET'])
def get_records():
    """
    Get all records from the database.
    """
    records = DataDepot.query.all()
    return jsonify([
        {
            "id": record.id,
            "name": record.name,
            "phone": record.phone,
            "email": record.email,
            "country": record.country,
            "region": record.region,
            "list": record.list,
            "alphanumeric": record.alphanumeric,
            "currency": record.currency,
            "numberrange": record.numberrange,
            "text": record.text,
            "postalZip": record.postalZip,
            "address": record.address,
        }
        for record in records
    ])

@app.route('/records', methods=['POST'])
def create_record():
    """
    Create a new record in the database.
    """
    data = request.json
    new_record = DataDepot(
        name=data['name'],
        phone=data['phone'],
        email=data['email'],
        country=data['country'],
        region=data['region'],
        list=data['list'],
        alphanumeric=data['alphanumeric'],
        currency=data['currency'],
        numberrange=data['numberrange'],
        text=data['text'],
        postalZip=data['postalZip'],
        address=data['address']
    )
    db.session.add(new_record)
    db.session.commit()
    return jsonify({"message": "Record created successfully", "record_id": new_record.id}), 201

@app.route('/records/<int:record_id>', methods=['PUT'])
def update_record(record_id):
    """
    Update an existing record in the database.
    """
    data = request.json
    record = DataDepot.query.get_or_404(record_id)
    record.name = data.get('name', record.name)
    record.phone = data.get('phone', record.phone)
    record.email = data.get('email', record.email)
    record.country = data.get('country', record.country)
    record.region = data.get('region', record.region)
    record.list = data.get('list', record.list)
    record.alphanumeric = data.get('alphanumeric', record.alphanumeric)
    record.currency = data.get('currency', record.currency)
    record.numberrange = data.get('numberrange', record.numberrange)
    record.text = data.get('text', record.text)
    record.postalZip = data.get('postalZip', record.postalZip)
    record.address = data.get('address', record.address)
    db.session.commit()
    return jsonify({"message": "Record updated successfully"})

@app.route('/records/<int:record_id>', methods=['DELETE'])
def delete_record(record_id):
    """
    Delete a record from the database.
    """
    record = DataDepot.query.get_or_404(record_id)
    db.session.delete(record)
    db.session.commit()
    return jsonify({"message": "Record deleted successfully"})

if __name__ == "__main__":
    app.run(debug=True)
