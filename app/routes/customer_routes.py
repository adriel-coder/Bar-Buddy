from flask import Blueprint
from app.controllers.customer_controller import list_customers, add_customer, get_customer, update_customer, delete_customer

customer_bp = Blueprint('customer_bp', __name__)

customer_bp.add_url_rule('/customers/', 'list_customers', list_customers, methods=['GET'])
customer_bp.add_url_rule('/customers/<int:customer_id>', 'get_customer', get_customer, methods=['GET'])
customer_bp.add_url_rule('/customers/', 'add_customer', add_customer, methods=['POST'])
customer_bp.add_url_rule('/customers/<int:customer_id>', 'update_customer', update_customer, methods=['PUT'])
customer_bp.add_url_rule('/customers/<int:customer_id>', 'delete_customer', delete_customer, methods=['DELETE'])
