from flask import jsonify, request
from app.models import Customer, db


def list_customers():
    customers = Customer.query.all()
    return jsonify([
        {
            "id": c.id,
            "name": c.name,
            "cpf": c.cpf,
            "phone": c.phone
        }
        for c in customers
    ]), 200

def add_customer():
    data = request.json

    existing_customer = Customer.query.filter_by(cpf=data['cpf']).first()
    if existing_customer:
        return jsonify({"error": "Customer with this cpf already exists"}), 400

    customer = Customer(
        name=data['name'],
        cpf=data['cpf'],
        phone=data['phone']
    )
    db.session.add(customer)
    db.session.commit()

    return jsonify({"message": "Customer added successfully!"}), 201


def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    return jsonify({
        "id": customer.id,
        "name": customer.name,
        "cpf": customer.cpf,
        "phone": customer.phone
    }), 200


def update_customer(customer_id):
    data = request.json
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    customer.name = data.get('name', customer.name)
    customer.cpf = data.get('cpf', customer.cpf)
    customer.phone = data.get('phone', customer.phone)

    db.session.commit()

    return jsonify({"message": "Customer updated successfully"}), 200


def delete_customer(customer_id):
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    db.session.delete(customer)
    db.session.commit()

    return jsonify({"message": "Customer deleted successfully"}), 200
