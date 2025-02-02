def test_add_waiter(client):
    """Testa a adição de um novo garçom"""
    response = client.post('/waiters/', json={
        "name": "Tiago Potter",
        "cpf": "532.746.490-31",
        "phone": "(31) 99876-5432"
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Waiter added successfully!"


def test_list_waiters(client, create_waiter):
    """Testa a listagem de garçons"""
    response = client.get('/waiters/')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_waiter(client, create_waiter):
    """Testa obter um garçom específico"""
    response = client.get(f'/waiters/{create_waiter.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == create_waiter.id
    assert data["name"] == "Luna Lovegood"


def test_update_waiter(client, create_waiter):
    """Testa atualizar um garçom"""
    response = client.put(f'/waiters/{create_waiter.id}', json={
        "name": "Neville Longbottom",
        "cpf": "581.013.020-85",
        "phone": "(31) 98365-1234"
    })
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Waiter updated successfully"


def test_delete_waiter(client, create_waiter):
    """Testa deletar um garçom"""
    response = client.delete(f'/waiters/{create_waiter.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Waiter deleted successfully"
