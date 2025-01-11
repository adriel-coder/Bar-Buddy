from .product_routes import product_bp
from .category_routes import category_bp
from .customer_routes import customer_bp
from .order_routes import order_bp
from .payment_routes import payment_bp
from .waiter_routes import waiter_bp
from .table_routes import table_bp

def register_routes(app):
    app.register_blueprint(product_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(customer_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(payment_bp)
    app.register_blueprint(waiter_bp)
    app.register_blueprint(table_bp)
