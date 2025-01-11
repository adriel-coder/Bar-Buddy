from flask import jsonify, request
from app.models import Table, db

def list_tables():
    tables = Table.query.all()

    return jsonify([
        {
            "id": t.id,
            "number": t.number,
            "status": t.status.value
        }
        for t in tables
    ])

def add_table():
    data = request.json
    existing_table = Table.query.filter_by(number=data['number']).first()
    if existing_table:
        return jsonify({"error": "Table with this number already exists"}), 400

    table = Table(number=data['number'], status=data['status'])
    db.session.add(table)
    db.session.commit()
    return jsonify({"message": "Table added successfully!"}), 201

def get_table(table_id):
    table = Table.query.filter_by(number=table_id).first()
    if not table:
        return jsonify({"error": "Table not found"}), 404

    return jsonify({
        "id": table.id,
        "number": table.number,
        "status": table.status.value
    }), 200

def update_table_status(table_id):
    data = request.json
    table = Table.query.get(table_id)
    if not table:
        return jsonify({"error": "Table not found"}), 404

    table.status = data.get('status', table.status)
    db.session.commit()
    return jsonify({"message": "Table status updated successfully!"}), 200

def delete_table(table_id):
    table = Table.query.get(table_id)
    if not table:
        return jsonify({"error": "Table not found"}), 404

    db.session.delete(table)
    db.session.commit()

    return jsonify({"message": "Table deleted successfully!"}), 200
