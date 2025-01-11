from flask import jsonify, request
from app.models import Category, db

def list_categories():
    categories = Category.query.all()

    return jsonify([{
        "id": c.id,
        "name": c.name,
        "products": [
            {
                "id": product.id,
                "name": product.name,
                "price": product.price
            }
            for product in c.products]}
        for c in categories])

def add_category():
    data = request.json
    existing_category = Category.query.filter_by(name=data['name']).first()
    if existing_category:
        return jsonify({"error": "Category with this name already exists"}), 400

    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({"message": "Category added successfully!"}), 201

def get_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"})
    
    products = [
        {
            "id": product.id,
            "name": product.name,
            "price": product.price
        }
        for product in category.products]
    
    return jsonify({
        "id": category.id,
        "name": category.name,
        "products": products
    }), 200

def update_category(category_id):
    data = request.json
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"}), 404
    
    category.name = data.get('name', category.name)

    db.session.commit()

    return jsonify({"message": "Category updated successfully"}), 200

def delete_category(category_id):
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Category not found"})
    
    db.session.delete(category)
    db.session.commit()
    
    return jsonify({"message": "Category deleted successfully"}), 200
