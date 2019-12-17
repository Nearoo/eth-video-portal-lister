from flask import Flask, request, abort
from requests import get
from urllib.parse import urlparse
from flask_cors import CORS
from flask_caching import Cache

app = Flask(__name__, static_folder="../public")

# Disable cross-origin
CORS(app)

# Enable caching
cache = Cache(config={'CACHE_TYPE': 'simple'})
cache.init_app(app)

@app.route("/")
def index():
    return app.send_static_file("index.html"), 404

@app.route("/eth-videoportal")
def video_portal():
    return app.send_static_file("eth-videoportal.html")

@app.route("/videoplayer")
def video_player():
    return app.send_static_file("videoplayer.html")
    

@app.route("/proxy-get")
def proxy_get():
    url = request.args.get("url", None)
    headers = {
        "Accept": "text/html",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    if url:
        if not cache.get(url):
            cache.set(url, get(url, headers=headers).content)
        return cache.get(url)
    else:
        abort(404)

@app.errorhandler(404)
def _404(_):
    return app.send_static_file("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000)