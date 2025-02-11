from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the simple HTTP server!"


@app.route('/post', methods=['POST'])
def post_data():
    data = request.form.get('data')  # Get the form data
    if data:
        print(f"Received data: {data}")  # Print the received data to the console
        return jsonify({"message": "Data received successfully", "data": data}), 201
    else:
        return jsonify({"error": "No data provided"}), 400


@app.route('/form', methods=['GET'])
def form():
    return render_template('form.html')  # Render the HTML form from the file


@app.route('/get', methods=['GET'])
def get_data():
    data = request.args.get('data')  # Get the query parameter 'data' from the GET request
    if data:
        print(f"Received data (GET): {data}")  # Print the received data to the console
        return jsonify({"message": "Data received successfully", "data": data}), 200
    else:
        return jsonify({"error": "No data provided in GET request"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
