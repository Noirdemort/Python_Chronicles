from flask import Flask, render_template, request, url_for

import random


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, world!" 

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.json:
        print(request.json['hey'])
    else:
        print(request.data)
    return "response recieved!"

if __name__ == '__main__':
    app.run(debug=True)
