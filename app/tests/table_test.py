def test_add_table(client):
    """Testa a adição de uma nova mesa"""
    response = client.post('/tables/', json={
        "number": 22,
        "status": "RESERVED"
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Table added successfully!"


def test_list_tables(client, create_table):
    """Testa a listagem de mesas"""
    response = client.get('/tables/')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_table(client, create_table):
    """Testa obter uma mesa específica"""
    response = client.get(f'/tables/{create_table.number}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == create_table.id
    assert data["number"] == 12


def test_update_table_status(client, create_table):
    """Testa atualizar o estado de uma mesa"""
    response = client.put(f'/tables/{create_table.id}', json={
        "status": "OCCUPIED"
    })
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Table status updated successfully!"


def test_delete_table(client, create_table):
    """Testa deletar uma mesa"""
    response = client.delete(f'/tables/{create_table.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Table deleted successfully!"
