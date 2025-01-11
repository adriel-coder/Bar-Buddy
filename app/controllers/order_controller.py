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
    order = Order(number=data['number'], customer_id=data['customer_id'], active=True)
    db.session.add(order)
    db.session.commit()
    return jsonify({"message": "Order created successfully!"}), 201

# Unused now
def close_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if not order.active:
        return jsonify({"error": "Order is already closed"})

    order.active = False
    db.session.commit()
    return jsonify({"message": "Order closed successfully!"}), 200

# Unused now
def activate_order(order_id):
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    if order.active:
        return jsonify({"error": "Order is already active"})

    order.active = True
    db.session.commit()
    return jsonify({"message": "Order activated successfully!"}), 200

def add_products_to_order(order_id):
    """
    Adiciona produtos a uma comanda (pedido).
    Se o produto já existir na comanda, soma a quantidade pedida à quantidade existente.
    """
    data = request.json

    # Verificar se a comanda existe
    order = Order.query.get(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404

    # Verificar se a comanda está ativa
    if not order.active:
        return jsonify({"error": "Order is not active"}), 400

    # Verificar se os produtos foram fornecidos
    products = data.get('products', [])
    if not products:
        return jsonify({"error": "No products provided"}), 400

    # Processar os produtos e atualizar ou adicionar na comanda
    total_added = 0
    for product_data in products:
        product_id = product_data.get('product_id')
        quantity = product_data.get('quantity')

        # Verificar se os dados do produto são válidos
        if not product_id or not quantity or quantity <= 0:
            return jsonify({"error": "Each product must have a valid 'product_id' and 'quantity' > 0"}), 400

        # Buscar o produto no banco
        product = Product.query.get(product_id)
        if not product:
            return jsonify({"error": f"Product with ID {product_id} not found"}), 404

        # Verificar se o produto já está na comanda
        order_item = OrderItem.query.filter_by(order_id=order.id, product_id=product_id).first()
        if order_item:
            # Atualizar a quantidade existente
            order_item.quantity += quantity
        else:
            # Adicionar um novo produto à comanda
            order_item = OrderItem(
                order_id=order.id,
                product_id=product.id,
                quantity=quantity
            )
            db.session.add(order_item)

        # Atualizar o total adicionado à comanda
        total_added += quantity * product.price

    # Atualizar o valor total da comanda
    order.total_amount += total_added
    db.session.commit()

    return jsonify({
        "message": "Products added to order successfully!",
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

    db.session.delete(order)
    db.session.commit()

    return jsonify({"message": "Order deleted successfully"}), 200
