import os
from flask import Flask, Response, request, send_file, send_from_directory, abort
from flask_cors import CORS
from .Controllers import controller

app = Flask(__name__)
app.config['filepath'] = 'src/static_content'
app.register_blueprint(controller,url_prefix="/files")
CORS(app)



@app.route("/health-check")
def index():
    return Response("Successful",200)

