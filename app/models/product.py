from app import db

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)  # Unique names for products
    price = db.Column(db.Float, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)

    category = db.relationship('Category', backref='products', lazy=True)
    items = db.relationship('OrderItem', backref='product', lazy=True)
