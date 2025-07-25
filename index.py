#main.py
from routes import index
from routes.admin import index as admin
from routes import login
from bottle import static_file, request, Bottle
from config import settings
from bottle_session import SessionPlugin

plugin = SessionPlugin(cookie_lifetime=600)
index.app.install(plugin)
login.app.install(plugin)
admin.app.install(plugin)

app = Bottle()

app.mount('/', index.app)
app.mount('/login', login.app) 
app.mount('/admin', admin.app)  


@app.hook('before_request')
def attach_custom_data():
    request.kdict = settings()

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

import socket    
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
if(addr == '127.0.1.1'):
    app.run(host='localhost', port=8000, debug=True, reloader=True)