from flask import Blueprint
from app.controllers.payment_controller import list_payments, add_payment, get_payment, update_payment, delete_payment


payment_bp = Blueprint('payment_bp', __name__)

payment_bp.add_url_rule('/payments/', 'list_payments', list_payments, methods=['GET'])
payment_bp.add_url_rule('/payments/', 'add_payment', add_payment, methods=['POST'])
payment_bp.add_url_rule('/payments/<int:payment_id>', 'get_payment', get_payment, methods=['GET'])
payment_bp.add_url_rule('/payments/<int:payment_id>', 'update_payment', update_payment, methods=['PUT'])
payment_bp.add_url_rule('/payments/<int:payment_id>', 'delete_payment', delete_payment, methods=['DELETE'])
