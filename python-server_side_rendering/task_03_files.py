from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def get_data(source):
    data = []
    if source == 'json':
        with open('products.json', 'r') as f:
            data = json.load(f)
    elif source == 'csv':
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # CSV-dən gələn hər şey stringdir, tip çevirmələri edirik
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                data.append(row)
    return data

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    error = None
    products = []

    # 1. Source yoxlanışı
    if source not in ['json', 'csv']:
        error = "Wrong source"
    else:
        # 2. Məlumatı oxu
        try:
            products = get_data(source)
            
            # 3. Əgər ID verilibsə, filtr et
            if product_id:
                filtered = [p for p in products if p['id'] == int(product_id)]
                if not filtered:
                    error = "Product not found"
                else:
                    products = filtered
        except Exception:
            error = "Data error"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
