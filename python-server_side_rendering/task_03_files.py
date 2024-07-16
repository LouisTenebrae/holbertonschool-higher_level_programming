from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def load_products_from_csv(filepath):
    products = []
    try:
        with open(filepath, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
    except Exception as e:
        return [], str(e)
    return products, None


def load_products_from_json(filepath):
    try:
        with open(filepath, mode='r') as file:
            products = json.load(file)
    except Exception as e:
        return [], str(e)
    return products, None


@app.route('/')
def index():
    return 'Welcome to the Flask App'


@app.route('/product_display')
def product_display():
    source = request.args.get('source', 'csv')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        error_message = 'Wrong source parameter. Use "json" or "csv".'
        return render_template('product_display.html',
                               error_message=error_message)

    if source == 'json':
        products, error = load_products_from_json('products.json')
    else:
        products, error = load_products_from_csv('products.csv')

    if error:
        return render_template('product_display.html', error_message=error)

    if product_id:
        product_id = int(product_id)
        filtered_products = [product for product in
                             products if product['id'] == product_id]
        if not filtered_products:
            error_message = f'Product not found with ID: {product_id}'
            return render_template('product_display.html',
                                   error_message=error_message)

        products = filtered_products

    return render_template('product_display.html', products=products)


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)
