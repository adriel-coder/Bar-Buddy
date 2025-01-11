from flask import Blueprint
from app.controllers.waiter_controller import (
    list_waiters, add_waiter, get_waiter, update_waiter, delete_waiter
)

waiter_bp = Blueprint('waiter_bp', __name__)

waiter_bp.add_url_rule('/waiters/', 'list_waiters', list_waiters, methods=['GET'])
waiter_bp.add_url_rule('/waiters/', 'add_waiter', add_waiter, methods=['POST'])
waiter_bp.add_url_rule('/waiters/<int:waiter_id>', 'get_waiter', get_waiter, methods=['GET'])
waiter_bp.add_url_rule('/waiters/<int:waiter_id>', 'update_waiter', update_waiter, methods=['PUT'])
waiter_bp.add_url_rule('/waiters/<int:waiter_id>', 'delete_waiter', delete_waiter, methods=['DELETE'])
