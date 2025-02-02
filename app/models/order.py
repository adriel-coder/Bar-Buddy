from datetime import datetime

from app import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(10), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    waiter_id = db.Column(db.Integer, db.ForeignKey('waiters.id'), nullable=True)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=True)
    active = db.Column(db.Boolean, default=True)
    total_amount = db.Column(db.Float, nullable=False, default=0.0)
    
    items = db.relationship('OrderItem', backref='order', lazy=True)
