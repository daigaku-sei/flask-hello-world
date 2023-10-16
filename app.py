from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/')
def whoami():
    return 'A demo of render app by daigakusei'
