#main.py
from routes import frontend
from bottle import static_file, request, Bottle
from db.connection import engine
from config import kdict

app = Bottle()

app.mount('/', frontend.app) 

@app.hook('before_request')
def attach_custom_data():
    request.engine = engine
    request.kdict = kdict

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/static')

import socket    
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
if(addr == '127.0.1.1'):
    app.run(host='localhost', port=8000, debug=True, reloader=True)