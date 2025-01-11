from flask import Blueprint
from app.controllers.product_controller import list_products, get_product, add_product, update_product, delete_product

product_bp = Blueprint('product_bp', __name__)

product_bp.add_url_rule('/products/', 'list_products', list_products, methods=['GET'])
product_bp.add_url_rule('/products/<int:product_id>', 'get_product', get_product, methods=['GET'])
product_bp.add_url_rule('/products/', 'add_product', add_product, methods=['POST'])
product_bp.add_url_rule('/products/<int:product_id>', 'update_product', update_product, methods=['PUT'])
product_bp.add_url_rule('/products/<int:product_id>', 'delete_product', delete_product, methods=['DELETE'])
