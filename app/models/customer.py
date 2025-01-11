from app import db

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
