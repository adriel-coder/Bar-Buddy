from flask import Blueprint
from app.controllers.order_controller import list_orders, add_order, change_status_order, add_products_to_order, \
    get_order, delete_order

order_bp = Blueprint('order_bp', __name__)

order_bp.add_url_rule('/orders/', 'list_orders', list_orders, methods=['GET'])
order_bp.add_url_rule('/orders/', 'add_order', add_order, methods=['POST'])
order_bp.add_url_rule('/orders/status/<int:order_id>', 'change_status_order', change_status_order, methods=['PUT'])
order_bp.add_url_rule('/orders/<int:order_id>/products', 'add_products_to_order', add_products_to_order, methods=['POST'])
order_bp.add_url_rule('/orders/<int:order_id>', 'get_order', get_order, methods=['GET'])
order_bp.add_url_rule('/orders/<int:order_id>', 'delete_order', delete_order, methods=['DELETE'])
