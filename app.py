from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

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
    app.run(debug=True)
