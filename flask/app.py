from flask import Flask

app = Flask(__name__, static_folder="../public")

@app.route("/")
def index():
    return "<p style='text-align: center;'>Nothing Here</p>"

@app.route("/eth-videoportal")
def video_portal():
    return app.send_static_file("video-lister")
    

app.run()