import pytest
import uuid
from app import create_app, db
from app.config import TestConfig
from app.models import Category, Product, Customer, Waiter, Table, Payment, Order, OrderItem


@pytest.fixture(scope="module")
def app():
    """Cria uma instância da aplicação Flask para testes"""
    app = create_app()
    app.config.from_object(TestConfig)  # Carrega configuração de testes

    with app.app_context():
        db.create_all()  # Cria tabelas no banco de testes
        yield app  # Retorna a aplicação para os testes
        db.session.remove()  # Remove a sessão do banco
        db.drop_all()  # Limpa o banco após os testes

@pytest.fixture
def client(app):
    """Cria um cliente de teste"""
    return app.test_client()

@pytest.fixture(scope="module")
def db_session(app):
    """Fornece uma sessão de banco de dados para os testes"""
    with app.app_context():
        yield db.session
        db.session.rollback()
        db.session.close()  # Fecha a sessão limpa


@pytest.fixture(scope="module")
def create_category(db_session):
    """Cria uma categoria antes de os testes serem executados"""
    category = Category(name="Refrigerantes")
    db_session.add(category)
    db_session.commit()
    return category  # Retorna a categoria criada para os testes

@pytest.fixture(scope="module")
def create_product(db_session, create_category):
    """Cria um produto antes de os testes serem executados"""
    product = Product(name="Guaraná Antártica", price=6.99, category_id=create_category.id)
    db_session.add(product)
    db_session.commit()

    return product  # Retorna o produto criado para os testes

@pytest.fixture(scope="module")
def create_customer(db_session):
    """Cria um cliente antes de os testes serem executados"""
    customer = Customer(name="Hermione Granger", cpf="190.346.050-60", phone="(19) 98251-2009")
    db_session.add(customer)
    db_session.commit()

    return customer

@pytest.fixture(scope="module")
def create_waiter(db_session):
    """Cria um cliente antes de os testes serem executados"""
    waiter = Waiter(name="Luna Lovegood", cpf="605.840.790-79", phone="(11) 99146-9249")
    db_session.add(waiter)
    db_session.commit()

    return waiter

@pytest.fixture(scope="module")
def create_table(db_session):
    """Cria um cliente antes de os testes serem executados"""
    table = Table(number=12)
    db_session.add(table)
    db_session.commit()

    return table

@pytest.fixture(scope="module")
def create_payment(db_session, create_order):
    """Cria um pagamento antes de os testes serem executados"""
    payment = Payment(order_id=create_order.id, payment_method="PIX")
    db_session.add(payment)
    db_session.commit()

    return payment

@pytest.fixture(scope="function")
def create_order(db_session, create_customer, create_waiter, create_table):
    """Cria uma comanda antes de os testes serem executados"""
    order = Order(
        number=str(uuid.uuid4())[:8],  # Um número aleatório para evitar duplicação nos testes
        customer_id=create_customer.id,
        waiter_id=create_waiter.id,
        table_id=create_table.id,
        active=True,
        total_amount=100.0
    )
    db_session.add(order)
    db_session.commit()

    return order

@pytest.fixture(scope="function")
def create_order_with_items(db_session, create_order, create_product):
    """Cria um pedido já com itens associados antes dos testes"""
    order_item = OrderItem(order_id=create_order.id, product_id=create_product.id, quantity=2)
    db_session.add(order_item)
    create_order.total_amount += create_product.price * 2
    db_session.commit()
    return create_order
