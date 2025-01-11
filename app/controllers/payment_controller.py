from datetime import timedelta

from flask import jsonify, request
from app.models import Payment, Order, db


def list_payments():
    payments = Payment.query.all()

    print()
    return jsonify([
        {
            "id": p.id,
            "order_id": p.order_id,
            "amount": p.order.total_amount,
            "payment_method": p.payment_method,
            "date": (p.date - timedelta(hours=3)).isoformat()
        }
        for p in payments
    ]), 200

def add_payment():
    data = request.json

    order = Order.query.get(data.get('order_id'))
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if Payment.query.filter_by(order_id=order.id).first():
        return jsonify({"error": "Payment for this order already exists"}), 400

    # Criar o pagamento
    payment = Payment(
        order_id=order.id,
        payment_method=data['payment_method']
    )

    order.active = False

    db.session.add(payment)
    db.session.commit()

    return jsonify({
        "message": "Payment added successfully!",
        "order_id": order.id,
        "order_total_amount": order.total_amount
    }), 201

def get_payment(payment_id):
    payment = Payment.query.get(payment_id)
    if not payment:
        return jsonify({"error": "Payment not found"}), 404

    return jsonify({
        "id": payment.id,
        "order_id": payment.order_id,
        "amount": payment.order.total_amount,
        "payment_method": payment.payment_method,
        "date": (payment.date - timedelta(hours=3)).isoformat()
    }), 200

def update_payment(payment_id):
    data = request.json
    payment = Payment.query.get(payment_id)

    if not payment:
        return jsonify({"error": "Payment not found"}), 404

    # Atualizar o método de pagamento
    payment.payment_method = data.get('payment_method', payment.payment_method)
    payment.date = data.get('date', payment.date)
    db.session.commit()

    return jsonify({"message": "Payment updated successfully!"}), 200

def delete_payment(payment_id):
    payment = Payment.query.get(payment_id)
    order = Order.query.get(payment.order_id)

    if not payment:
        return jsonify({"error": "Payment not found"}), 404

    order.active = True

    db.session.delete(payment)
    db.session.commit()

    return jsonify({"message": "Payment deleted successfully!"}), 200
