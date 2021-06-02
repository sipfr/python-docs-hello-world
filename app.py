from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def hello():
    image_list = [ f for f in os.listdir('/')  ]
    return image_list

