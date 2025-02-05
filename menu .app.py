from flask import Flask, request, jsonify

app = Flask(__name__)

menu = [
    {"Name": "Chicken Noodles", "Price": 180},
    {"Name": "Chicken Rice", "Price": 150},
    {"Name": "Naan with Chicken Tikka Masala", "Price": 200}
]

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        menu.append(data)
    return jsonify(menu)

if __name__ == '__main__':
    app.run(debug=True)

    
