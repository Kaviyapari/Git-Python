from flask import Flask, request, jsonify

app = Flask(__name__)

Dinnermenu = [
    {"Name": "Chicken Noodles", "Price": 180},
    {"Name": "Chicken Rice", "Price": 150},
    {"Name": "Naan with Chicken Tikka Masala", "Price": 200},
    {"Name": "Boratta","Price": 40}
]

@app.route('/data', methods=['GET', 'POST'])
def handle_data():
    if request.method == 'POST':
        data = request.get_json()
        Dinnermenu.append(data)
    return jsonify(Dinnermenu)

if __name__ == '__main__':
    app.run(debug=True)

    
