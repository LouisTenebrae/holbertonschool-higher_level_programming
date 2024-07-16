import json
from flask import Flask, render_template

app = Flask(__name__)


def load_items_from_json():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            return data.get('items', [])
    except FileNotFoundError:
        return []


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


if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)