from flask import Blueprint
from app.controllers.category_controller import list_categories, get_category, add_category, update_category, delete_category


category_bp = Blueprint('category_bp', __name__)

category_bp.add_url_rule('/categories/', 'list_categories', list_categories, methods=['GET'])
category_bp.add_url_rule('/categories/<int:category_id>', 'get_product', get_category, methods=['GET'])
category_bp.add_url_rule('/categories/', 'add_category', add_category, methods=['POST'])
category_bp.add_url_rule('/categories/<int:category_id>', 'update_product', update_category, methods=['PUT'])
category_bp.add_url_rule('/categories/<int:category_id>', 'delete_product', delete_category, methods=['DELETE'])
