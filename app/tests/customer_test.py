def test_add_customer(client):
    """Testa a adição de um novo cliente"""
    response = client.post('/customers/', json={
        "name": "Ronald Wesley",
        "cpf": "940.920.790-87",
        "phone": "(11) 99027-6568"
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Customer added successfully!"


def test_list_customers(client, create_customer):
    """Testa a listagem de clientes"""
    response = client.get('/customers/')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_customer(client, create_customer):
    """Testa obter um cliente específico"""
    response = client.get(f'/customers/{create_customer.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == create_customer.id
    assert data["name"] == "Hermione Granger"


def test_update_customer(client, create_customer):
    """Testa atualizar um cliente"""
    response = client.put(f'/customers/{create_customer.id}', json={
        "name": "Lúcio Malfoy",
        "cpf": "267.333.150-68",
        "phone": "(21) 98765-1234"
    })
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Customer updated successfully"


def test_delete_customer(client, create_customer):
    """Testa deletar um cliente"""
    response = client.delete(f'/customers/{create_customer.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Customer deleted successfully"
