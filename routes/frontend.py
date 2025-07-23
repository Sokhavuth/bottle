#routes/index.py
#import config
from copy import deepcopy
from bottle import Bottle, template, request

app = Bottle()

@app.route('/')
def index():
    kdict = request.kdict
    return template('home', data=kdict)