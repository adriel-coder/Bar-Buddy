from flask import Blueprint
from app.controllers.table_controller import list_tables, add_table, get_table, update_table_status, delete_table

table_bp = Blueprint('table_bp', __name__)

table_bp.add_url_rule('/tables/', 'list_tables', list_tables, methods=['GET'])
table_bp.add_url_rule('/tables/', 'add_table', add_table, methods=['POST'])
table_bp.add_url_rule('/tables/<int:table_number>', 'get_table', get_table, methods=['GET'])
table_bp.add_url_rule('/tables/<int:table_id>', 'update_table_status', update_table_status, methods=['PUT'])
table_bp.add_url_rule('/tables/<int:table_id>', 'delete_table', delete_table, methods=['DELETE'])
