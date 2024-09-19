from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/clean_url', methods=['POST'])
def clean_url():
    data = request.json
    url = data.get('url', '')
    
    # Parse the URL
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)

    # Remove csrfToken and its value
    if 'csrfToken' in query_params:
        del query_params['csrfToken']

    # Rebuild the URL with cleaned query parameters
    cleaned_query = urlencode(query_params, doseq=True)
    cleaned_url = urlunparse((
        parsed_url.scheme,
        parsed_url.netloc,
        parsed_url.path,
        parsed_url.params,
        cleaned_query,
        parsed_url.fragment
    ))

    return jsonify({'cleaned_url': cleaned_url})

if __name__ == '__main__':
    # Allow external access on the local network
    app.run(host='0.0.0.0', port=5000, debug=True)
