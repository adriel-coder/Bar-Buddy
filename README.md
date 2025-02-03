# BarBuddy Project

**BarBuddy** é um sistema backend para gerenciamento de comandas e pedidos em bares ou restaurantes, desenvolvido em **Python** utilizando o framework **Flask** e SQLAlchemy como ORM.

---

## Funcionalidades

- Gerenciamento de **clientes**, **produtos**, **pedidos** e **categorias**.
- Sistema de **comandas** que permite:
  - Adicionar e listar produtos nas comandas.
  - Alterar o status das comandas.
- Sistema de **pagamentos**:
  - Gerenciamento de métodos de pagamento.
  - Registro de pagamentos vinculados a pedidos.
- Rotas RESTful organizadas e seguras.
- Banco de dados relacional.

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Framework**: Flask
- **Banco de Dados**: MySQL
- **ORM**: SQLAlchemy
- **Biblioteca Adicional**:
  - `Flask-SQLAlchemy` para abstração do banco de dados

---

## Estrutura do Projeto

```
BarBuddy Project/
├── app/
│   ├── __init__.py          # Inicialização da aplicação
│   ├── models/              # Modelos de dados (ORM)
│   │   ├── __init__.py
│   │   ├── order.py
│   │   ├── payment.py
│   │   ├── product.py
|   |   ├── customer.py
|   |   ├── waiter.py
|   |   ├── table.py
|   |   ├── order_item.py
│   │   └── category.py
│   ├── controllers/         # Lógica de negócios (Controllers)
│   │   ├── __init__.py
│   │   ├── order_controller.py
│   │   ├── payment_controller.py
│   │   ├── product_controller.py
│   │   ├── customer_controller.py
│   │   ├── table_controller.py
│   │   ├── waiter_controller.py
│   │   └── category_controller.py
│   ├── routes/              # Rotas e blueprints
│   │   ├── __init__.py
│   │   ├── order_routes.py
│   │   ├── category_routes.py
│   │   ├── customer_routes.py
│   │   ├── payment_routes.py
│   │   ├── waiter_routes.py
│   │   ├── table_routes.py
│   │   └── product_routes.py
|   ├── tests/               # Testes unitários
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── order_test.py
│   │   ├── category_test.py
│   │   ├── customer_test.py
│   │   ├── payment_test.py
│   │   ├── waiter_test.py
│   │   ├── table_test.py
│   │   └── product_test.py
│   └── config.py            # Configurações da aplicação
├── run.py                   # Ponto de entrada da aplicação
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do projeto
```

---

## Configuração do Ambiente

### 1. Clone o repositório:
```bash
git clone https://github.com/adriel-coder/Bar-Buddy.git
cd Bar-Buddy
```

### 2. Crie e ative um ambiente virtual:
```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados:
- Tenha um servidor MySQL instalado e crie o banco de dados 'bar_buddy' se não existir.
- Atualize o arquivo `app/config.py` com as credenciais do seu banco de dados.

### 5. Execute o servidor:
```bash
python run.py
```

O servidor estará disponível em: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Testes

Atualmente, o sistema não possui uma suite de testes automatizados. Recomenda-se utilizar ferramentas como **pytest** ou **unittest** para validação futura.

---

## Licença

Este projeto é licenciado sob a [MIT License](https://opensource.org/licenses/MIT).

---

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório do projeto.
