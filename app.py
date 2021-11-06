
# -*- coding: utf-8 -*-

# flask_web/app.py

from flask import Flask
import json

app = Flask(__name__)

@app.route('/helloworld')

def index():
    data =  {
        "Hello" : "World"
    }
    return json.dumps(data)

@app.route('/')
def say_hello():
    data =  {}
    return '<h1>Hello, Flask!</h1>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

