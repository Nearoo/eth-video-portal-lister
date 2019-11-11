from flask import Flask, request, abort
from requests import get

app = Flask(__name__, static_folder="../public")

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
    url = request.args["url"]
    headers = {
        "Accept": "text/html",
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    }
    if url:
        return get(url, headers=headers).content
    else:
        abort(404)

@app.errorhandler(404)
def _404(_):
    return app.send_static_file("404.html"), 404

app.run(debug=False)