from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Item(db.Model):
    __tablename__ = 'datadepot_db'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # AUTO_INCREMENT (SERIAL) w PostgreSQL
    name = db.Column(db.String(255), nullable=False)  # VARCHAR(255)
    phone = db.Column(db.String(100), nullable=True)  # VARCHAR(100)
    email = db.Column(db.String(255), nullable=True)  # VARCHAR(255)
    country = db.Column(db.String(100), nullable=True)  # VARCHAR(100)
    region = db.Column(db.String(50), nullable=True)  # VARCHAR(50)
    list = db.Column(db.String(255), nullable=True)  # VARCHAR(255)
    alphanumeric = db.Column(db.String(255), nullable=True)  # VARCHAR(255)
    currency = db.Column(db.String(100), nullable=True)  # VARCHAR(100)
    numberrange = db.Column(db.Integer, nullable=True)  # INT
    text = db.Column(db.Text, nullable=True)  # TEXT
    postalZip = db.Column(db.String(10), nullable=True)  # VARCHAR(10)
    address = db.Column(db.String(255), nullable=True)  # VARCHAR(255)

    def __repr__(self):
        return f"<Item {self.name}>"
