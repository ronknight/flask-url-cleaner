# 🧹 [Flask URL Cleaner](https://github.com/ronknight/flask-url-cleaner)

#### A simple Flask web application that removes the 'csrfToken' parameter from URLs.

<p align="center">
  <a href="#features">Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installation">Installation</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#usage">Usage</a> •
  <a href="#api-endpoint">API Endpoint</a> •
  <a href="#example">Example</a> •
  <a href="#web-interface">Web Interface</a>
</p>

---

## 🌟 Features

- Removes the 'csrfToken' parameter from URLs
- Simple Flask web application with a user interface
- API endpoint for programmatic access
- Easily integrable into larger projects

## 📋 Requirements

- Python 3.x
- Flask

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ronknight/flask-url-cleaner.git
   cd flask-url-cleaner
   ```

2. Install the required dependencies:
   ```bash
   pip install flask
   ```

## 📁 Project Structure

The project has the following structure:

```
flask-url-cleaner/
│
├── app.py
├── README.md
└── index.html
```

- `app.py`: The main Flask application file
- `README.md`: This file, containing project information and instructions
- `index.html`: The HTML template for the web interface

## 🚀 Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. The server will start running on `http://127.0.0.1:5000/` and will be accessible on your local network.

3. Open your web browser and navigate to `http://127.0.0.1:5000/` or use your local network IP address to access the application from other devices.

## 📡 API Endpoint

### POST /clean_url

Removes the 'csrfToken' parameter from the provided URL.

**Request Body:**
```json
{
    "url": "https://example.com/page?param1=value1&csrfToken=abc123&param2=value2"
}
```

**Response:**
```json
{
    "cleaned_url": "https://example.com/page?param1=value1&param2=value2"
}
```

## 💡 Example

Using curl to test the API:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"url": "https://example.com/page?param1=value1&csrfToken=abc123&param2=value2"}' http://127.0.0.1:5000/clean_url
```

Expected output:
```json
{
    "cleaned_url": "https://example.com/page?param1=value1&param2=value2"
}
```

## 🌐 Web Interface

The application includes a web interface for easy URL cleaning:

1. Open your web browser and go to `http://127.0.0.1:5000/` or use your local network IP address (e.g., `http://10.0.6.105:5000/`)
2. You'll see a form with the title "Enter a URL to Clean"
3. Enter the URL you want to clean in the provided input field
4. Click the "Clean URL" button
5. The cleaned URL will be displayed in the "Response" section below the form

The web interface is rendered using the `index.html` file located in the root directory. Flask serves this file directly from the root directory when you navigate to the root URL `/`.

---

Made with ❤️ by [Ronknight](https://github.com/ronknight)
