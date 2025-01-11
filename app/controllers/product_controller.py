from flask import jsonify, request
from app.models import Product, Category, db

def list_products():
    products = Product.query.all()
    
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "category": p.category.name if p.category else None
        }
        for p in products])

def add_product():
    data = request.json
    existing_product = Product.query.filter_by(name=data['name']).first()
    if existing_product:
        return jsonify({"error": "Product with this name already exists"}), 400

    product = Product(name=data['name'], price=data['price'], category_id=data['category_id'])

    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added successfully!"}), 201

def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    category_name = product.category.name if product.category else None

    return jsonify(
        {
            "id": product.id,
            "name": product.name,
            "price": product.price,
            "category": category_name
        }), 200

def update_product(product_id):
    data = request.json
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    product.name = data.get('name', product.name)  
    product.price = data.get('price', product.price)  
    category_id = data.get('category_id')
    
    if category_id is not None:
        category = Category.query.get(category_id)
        if not category:
            return jsonify({"error": "Category not found"}), 404
        product.category_id = category.id

    db.session.commit()

    return jsonify({"message": "Product updated successfully"}), 200

def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({"message": "Product deleted successfully"}), 200
