from  . import app
from .factory import AppFactory
from .error_handler import EcommerceException
from flask import jsonify, request
import re
import os

_database = AppFactory.db
_collection = _database.collection('products')

@app.route('/api/products')
def serveProducts():
    print("Fetching Products")
    query = _collection.stream()
    print("Products fetched")
    products = []
    for q in query:
        products.append({'id':q.id,'data':q.to_dict()})
    return jsonify({'status_code':200,'products':products})

@app.route('/api/products', methods=['POST'])
def addProduct():
    _fields = AppFactory.constants['base_fields']
    _field_keys = list(_fields.keys()) 
    _form_keys = list(request.args)
    missingFields = set(_field_keys) - set(_form_keys)
    missingFields = list(missingFields)
    # Lets just trust the client for now
    if len(missingFields):
        raise EcommerceException(name = "Missing Fields", description = {'description':'Supply all fields','missing_field':missingFields,'supplied_fields':_form_keys})
    # Will not reach here on err
    name = request.args['product_name']
    name_slug = re.sub('[^a-zA-Z0-9]','-',name)
    data = dict(request.args)
    data['slug'] = name_slug
    _collection.document().set(data)
    return jsonify({'status_code':200,'status-info':'Success','product-slug':name_slug})


# @app.route('/categories')
# def listCategories():
#     print("Fetching Products")
#     query = _collection.stream()
#     print("Products fetched")
#     categories = []
#     for q in query:
#         products.append(q.to_dict()['category'])
#     return jsonify({'status_code':200,'categories':categories})

# @app.route('/categories/<category_slug>')
# def productsInCategory():
#     print("Fetching Products")
#     query = _collection.stream()
#     print("Products fetched")
#     categories = []
#     for q in query:
#         products.append(q.to_dict()['category'])
#     return jsonify({'status_code':200,'categories':categories})