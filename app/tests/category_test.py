def test_add_category(client):
    """Testa a adição de uma nova categoria"""
    response = client.post('/categories/', json={"name": "Pratos"})
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Category added successfully!"

def test_list_categories(client):
    """Testa a listagem de categorias"""
    response = client.get('/categories/')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_category(client, db_session, create_category):
    """Testa obter uma categoria específica"""
    response = client.get(f'/categories/{create_category.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == create_category.id
    assert data["name"] == "Refrigerantes"

def test_update_category(client, db_session, create_category):
    """Testa atualizar uma categoria"""
    response = client.put(f'/categories/{create_category.id}', json={"name": "Entradas"})
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Category updated successfully"

def test_delete_category(client, db_session, create_category):
    """Testa deletar uma categoria"""
    response = client.delete(f'/categories/{create_category.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Category deleted successfully"
