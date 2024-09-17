<h1 align="center">🧹 <a href="https://github.com/ronknight/flask-url-cleaner">Flask URL Cleaner</a></h1>

<h4 align="center">A simple Flask API that removes the 'csrfToken' parameter from URLs.</h4>

<p align="center">
<a href="https://twitter.com/PinoyITSolution"><img src="https://img.shields.io/twitter/follow/PinoyITSolution?style=social"></a>
<a href="https://github.com/ronknight?tab=followers"><img src="https://img.shields.io/github/followers/ronknight?style=social"></a>
<a href="https://github.com/ronknight/ronknight/stargazers"><img src="https://img.shields.io/github/stars/BEPb/BEPb.svg?logo=github"></a>
<a href="https://github.com/ronknight/ronknight/network/members"><img src="https://img.shields.io/github/forks/BEPb/BEPb.svg?color=blue&logo=github"></a>
<a href="https://youtube.com/@PinoyITSolution"><img src="https://img.shields.io/youtube/channel/subscribers/UCeoETAlg3skyMcQPqr97omg"></a>
<a href="https://github.com/ronknight/flask-url-cleaner/issues"><img src="https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat"></a>
<a href="https://github.com/ronknight/flask-url-cleaner/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg"></a>
<a href="#"><img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg"></a>
<a href="https://github.com/ronknight"><img src="https://img.shields.io/badge/Made%20with%20%F0%9F%A4%8D%20by%20-%20Ronknight%20-%20red"></a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#requirements">Requirements</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#api-endpoint">API Endpoint</a> •
  <a href="#example">Example</a>
</p>

---

## 🌟 Features

- Removes the 'csrfToken' parameter from URLs
- Simple Flask API with a single endpoint
- Easily integrable into larger projects

## 📋 Requirements

- Python 3.x
- Flask

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/ronknight/flask-url-cleaner.git
   cd flask-url-cleaner
   ```

2. Install the required dependencies:
   ```
   pip install flask
   ```

## 🚀 Usage

1. Run the Flask application:
   ```
   python app.py
   ```

2. The server will start running on `http://127.0.0.1:5000/`

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

---

Made with ❤️ by [Ronknight](https://github.com/ronknight)