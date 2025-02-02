def test_add_product(client, create_category):
    """Testa a adição de um novo produto usando uma categoria existente"""
    response = client.post('/products/', json={
        "name": "Pepsi 350ml",
        "price": 7.99,
        "category_id": create_category.id
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Product added successfully!"

def test_list_products(client, create_product):
    """Testa a listagem de produtos"""
    response = client.get('/products/')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_product(client, create_product):
    """Testa obter um produto específico"""
    response = client.get(f'/products/{create_product.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == create_product.id
    assert data["name"] == "Guaraná Antártica"

def test_update_product(client, create_product):
    """Testa atualizar um produto"""
    response = client.put(f'/products/{create_product.id}', json={
        "name": "Coca Cola 350ml",
        "price": 9.99
    })
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Product updated successfully"

def test_delete_product(client, create_product):
    """Testa deletar um produto"""
    response = client.delete(f'/products/{create_product.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Product deleted successfully"
