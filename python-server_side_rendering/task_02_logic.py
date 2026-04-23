from flask import Flask, render_template
import json

app = Flask(__name__)

# Əvvəlki tapşırıqdan qalan marşrutları da burada saxlaya bilərsiniz
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    try:
        # JSON faylını oxuyuruq
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fayl tapılmazsa və ya xətalıdırsa, boş siyahı kimi davranırıq
        items_list = []
        
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
