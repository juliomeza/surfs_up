# import flask library
from flask import Flask

# create a new flask instance
app = Flask(__name__)

# Create flask route
@app.route('/')
def hello_world():
    return 'Hellow World'

