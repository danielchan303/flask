
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def hello_world():
    method_post = request.method == 'POST'


    return render_template("layout.html", name=request['name'])
