import csv
import json
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_file():
    with open('products.json', 'r') as json_file:
        data = json.load(json_file)
    return data


def read_csv_file():
    data = []
    with open('products.csv', 'r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            data.append(row)
    return data


def read_sql_data():
    data = []
    try:
        conn = sqlite3.connect('products.db')
        c = conn.cursor()
        c.execute('SELECT id, name, category, price FROM products')
        rows = c.fetchall()
        for row in rows:
            data.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        conn.close()
    except sqlite3.Error as e:
        return [], str(e)
    return data, None


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        items_data = json.load(f)
    items_list = items_data.get('items', [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error='Wrong source')

    data = []
    if source == 'json':
        data = read_json_file()
    elif source == 'csv':
        data = read_csv_file()
    elif source == 'sql':
        data, error = read_sql_data()
        if error:
            return render_template('product_display.html', error=error)

    if product_id:
        filtered_data = [product for product in data
                         if str(product['id']) == product_id]
        if not filtered_data:
            return render_template('product_display.html',
                                   error='Product not found')
        data = filtered_data

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
