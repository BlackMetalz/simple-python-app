# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Init the data store for testing
data_store = {}

@app.route('/', methods=['GET'])
def hello():
    return "Hello simple python flask app!. Version 2.0"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/data', methods=['PUT'])
def put_data():
    data = request.json
    data_store.update(data)
    return jsonify(data_store), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)