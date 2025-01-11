from app import db
from datetime import datetime

class Payment(db.Model):
    __tablename__ = 'payments'
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    order = db.relationship('Order', backref='payments', lazy=True)
