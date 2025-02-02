def test_add_order(client, create_customer, create_waiter, create_table):
    """Testa a criação de um pedido"""
    response = client.post('/orders/', json={
        "number": "ORD123",
        "customer_id": create_customer.id,
        "waiter_id": create_waiter.id,
        "table_id": create_table.id
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Order created successfully"


def test_list_orders(client, create_order_with_items):
    """Testa a listagem de pedidos"""
    response = client.get('/orders/')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_order(client, create_order_with_items):
    """Testa a recuperação de um pedido específico"""
    response = client.get(f'/orders/{create_order_with_items.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == create_order_with_items.id
    assert "products" in data
    assert len(data["products"]) > 0


def test_add_products_to_order(client, create_order, create_product):
    """Testa a adição de produtos a um pedido"""
    response = client.post(f'/orders/{create_order.id}/products', json={
        "products": [{"product_id": create_product.id, "quantity": 3}]
    })
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Products added to order successfully"
    assert data["total_added"] == create_product.price * 3
    assert data["order_id"] == create_order.id


def test_change_status_order(client, create_order_with_items):
    """Testa a mudança do estado de um pedido"""
    response = client.put(f'/orders/status/{create_order_with_items.id}', json={"active": False})
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Order closed successfully"


def test_delete_order(client, create_order_with_items):
    """Testa a remoção de um pedido"""
    response = client.delete(f'/orders/{create_order_with_items.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Order deleted successfully"
