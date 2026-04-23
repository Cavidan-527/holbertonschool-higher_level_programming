from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def get_sql_data():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row  # Sütun adları ilə daxil olmağa imkan verir
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Products")
    rows = cursor.fetchall()
    # Row obyektlərini dictionary formatına çeviririk
    data = [dict(row) for row in rows]
    conn.close()
    return data

def get_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def get_csv_data():
    data = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            data.append(row)
    return data

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    products = []
    error = None

    # Məlumat mənbəyini seçirik
    try:
        if source == 'json':
            products = get_json_data()
        elif source == 'csv':
            products = get_csv_data()
        elif source == 'sql':
            products = get_sql_data()
        else:
            error = "Wrong source"
    except Exception:
        error = "Data source error"

    # Əgər id verilibsə, filtr edirik
    if not error and product_id:
        filtered = [p for p in products if p['id'] == int(product_id)]
        if not filtered:
            error = "Product not found"
        else:
            products = filtered

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
