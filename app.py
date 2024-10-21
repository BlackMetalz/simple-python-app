from flask import Flask, request, jsonify, Response
from prometheus_flask_exporter import PrometheusMetrics
from flask_basicauth import BasicAuth
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path)
else:
    print("No .env file found")

# Give the app a name
app = Flask(__name__)

# Init the data store for testing
data_store = {}

# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)

# Configure Basic Auth using environment variables
app.config['BASIC_AUTH_USERNAME'] = os.getenv('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.getenv('BASIC_AUTH_PASSWORD')
basic_auth = BasicAuth(app)

# Print the loaded environment variables for debugging
print(f"Loaded BASIC_AUTH_USERNAME: {app.config['BASIC_AUTH_USERNAME']}")
print(f"Loaded BASIC_AUTH_PASSWORD: {app.config['BASIC_AUTH_PASSWORD']}")

# Protect the /metrics endpoint with basic auth
@app.before_request
def before_request():
    if request.path == '/metrics':
        auth = request.authorization
        if not auth or not (auth.username == app.config['BASIC_AUTH_USERNAME'] and auth.password == app.config['BASIC_AUTH_PASSWORD']):
            return Response(
                'Could not verify your access level for that URL.\n'
                'You have to login with proper credentials', 401,
                {'WWW-Authenticate': 'Basic realm="Login Required"'})


@app.route('/', methods=['GET'])
def hello():
    return "Hello simple python flask app!. Version 3.0 include exporter!"

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

@app.route('/data', methods=['PUT'])
def put_data():
    data = request.json
    data_store.update(data)
    return jsonify(data_store), 201

# Route that returns a 4xx response
@app.route('/bad_request', methods=['GET'])
def bad_request():
    return jsonify({"error": "This is a bad request"}), 400

# Route that returns a 5xx response
@app.route('/server_error', methods=['GET'])
def server_error():
    return jsonify({"error": "This is a server error"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)