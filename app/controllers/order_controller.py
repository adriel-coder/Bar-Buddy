from flask import jsonify, request

from app.models import Order, db
from app.models.order_item import OrderItem
from app.models.product import Product

def list_orders():
    orders = Order.query.all()
    return jsonify([
        {
            "id": o.id, 
            "number": o.number, 
            "customer_id": o.customer_id, 
            "active": o.active,
            "total_amount": o.total_amount,
            "products": [
                {
                    "id": item.product_id,
                    "name": item.product.name,
                    "quantity": item.quantity
                }
                for item in o.items
            ]
        } 
        for o in orders
    ])

def add_order():
    data = request.json
    order = Order(
        number=data['number'],
        customer_id=data['customer_id'],
        waiter_id=data['waiter_id'],
        table_id=data['table_id']
        )
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order created successfully"}), 201


def update_order(order_id):
    """Atualiza um pedido existente"""
    data = request.json
    order = Order.query.get(order_id)

    if not order:
        return jsonify({"error": "Order not found"}), 404

    order.customer_id = data.get('customer_id', order.customer_id)
    order.waiter_id = data.get('waiter_id', order.waiter_id)
    order.table_id = data.get('table_id', order.table_id)

    db.session.commit()

    return jsonify({"message": "Order updated successfully"}), 200


def change_status_order(order_id):
    data = request.json
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if data.get("active") == order.active:
        return jsonify({"error": "Order status not modified"}), 304
    else:
        order.active = data.get("active")

    db.session.commit()

    status = 'activated' if order.active else 'closed'

    return jsonify({"message": f"Order {status} successfully"}), 200

def add_products_to_order(order_id):
    data = request.json

    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if not order.active:
        return jsonify({"error": "Order is not active"}), 400

    products = data.get('products', [])
    if not products:
        return jsonify({"error": "No products provided"}), 400

    total_added = 0
    for product_data in products:
        product_id = product_data.get('product_id')
        quantity = product_data.get('quantity')

        if not product_id or not quantity or quantity <= 0:
            return jsonify({"error": "Each product must have a valid 'product_id' and 'quantity' > 0"}), 400

        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": f"Product with ID {product_id} not found"}), 404

        order_item = OrderItem.query.filter_by(order_id=order.id, product_id=product_id).first()
        if order_item:
            order_item.quantity += quantity
        else:
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity
            )
            db.session.add(order_item)

        total_added += quantity * product.price

    order.total_amount += total_added
    db.session.commit()

    return jsonify({
        "message": "Products added to order successfully",
        "total_added": total_added,
        "order_id": order.id
    }), 200

def get_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(
        {
            "id": order.id,
            "number": order.number,
            "customer_id": order.customer_id,
            "active": order.active,
            "total_amount": order.total_amount,
            "products": [
                {
                    "id": item.product_id,
                    "name": item.product.name,
                    "quantity": item.quantity
                }
                for item in order.items
            ]
        }
    ), 200

def delete_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Remove os itens antes de deletar o pedido
    OrderItem.query.filter_by(order_id=order_id).delete()

    db.session.delete(order)
    db.session.commit()

    return jsonify({"message": "Order deleted successfully"}), 200

# TODO uma função para remover produtos da comanda atualizando a conta total
