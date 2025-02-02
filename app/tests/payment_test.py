from datetime import datetime


def test_add_payment(client, create_order):
    """Testa a criação de um novo pagamento"""
    response = client.post('/payments/', json={
        "order_id": create_order.id,
        "payment_method": "Credit Card"
    })
    data = response.get_json()

    assert response.status_code == 201
    assert data["message"] == "Payment added successfully"


def test_list_payments(client, create_payment):
    """Testa a listagem de pagamentos"""
    response = client.get('/payments/')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)


def test_get_payment(client, create_payment):
    """Testa obter um pagamento específico"""
    response = client.get(f'/payments/{create_payment.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["id"] == create_payment.id
    assert data["payment_method"] == "PIX"

def test_update_payment(client, create_payment):
    """Testa atualizar uma categoria"""
    response = client.put(f'/payments/{create_payment.id}', json={
        "payment_method": "Debit Card",
        "date": str(datetime(2025, 1, 31, 20, 30, 00))
    })
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Payment updated successfully"


def test_delete_payment(client, create_payment):
    """Testa deletar um pagamento"""
    response = client.delete(f'/payments/{create_payment.id}')
    data = response.get_json()

    assert response.status_code == 200
    assert data["message"] == "Payment deleted successfully"
