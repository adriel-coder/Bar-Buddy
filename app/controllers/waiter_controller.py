from flask import jsonify, request
from app.models import Waiter, db


def list_waiters():
    waiters = Waiter.query.all()
    return jsonify([
        {
            "id": w.id,
            "name": w.name,
            "cpf": w.cpf,
            "phone": w.phone
        }
        for w in waiters
    ]), 200

def add_waiter():
    data = request.json

    existing_waiter = Waiter.query.filter_by(cpf=data['cpf']).first()
    if existing_waiter:
        return jsonify({"error": "Waiter with this CPF already exists"}), 400

    waiter = Waiter(
        name=data['name'],
        cpf=data['cpf'],
        phone=data['phone']
    )
    db.session.add(waiter)
    db.session.commit()

    return jsonify({
        "message": "Waiter added successfully!",
        "waiter": {
            "id": waiter.id,
            "name": waiter.name,
            "cpf": waiter.cpf,
            "phone": waiter.phone
        }
    }), 201

def get_waiter(waiter_id):
    waiter = Waiter.query.get(waiter_id)
    if not waiter:
        return jsonify({"error": "Waiter not found"}), 404

    return jsonify({
        "id": waiter.id,
        "name": waiter.name,
        "cpf": waiter.cpf,
        "phone": waiter.phone
    }), 200

def update_waiter(waiter_id):
    data = request.json
    waiter = Waiter.query.get(waiter_id)
    if not waiter:
        return jsonify({"error": "Waiter not found"}), 404

    if 'cpf' in data and data['cpf'] != waiter.cpf:
        existing_waiter = Waiter.query.filter_by(cpf=data['cpf']).first()
        if existing_waiter and existing_waiter.id != waiter_id:
            return jsonify({"error": "CPF is already in use by another waiter"}), 400

    waiter.name = data.get('name', waiter.name)
    waiter.cpf = data.get('cpf', waiter.cpf)
    waiter.phone = data.get('phone', waiter.phone)

    db.session.commit()

    return jsonify({"message": "Waiter updated successfully"}), 200

def delete_waiter(waiter_id):
    waiter = Waiter.query.get(waiter_id)
    if not waiter:
        return jsonify({"error": "Waiter not found"}), 404

    db.session.delete(waiter)
    db.session.commit()

    return jsonify({"message": "Waiter deleted successfully"}), 200
