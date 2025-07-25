#main.py
from routes import index
from routes.admin import index as admin
from routes import login
from bottle import static_file, request, Bottle
from config import settings
import os, jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from dotenv import load_dotenv
load_dotenv()

app = Bottle()

app.mount('/', index.app)
app.mount('/login', login.app) 
app.mount('/admin', admin.app)  


@app.hook('before_request')
def attach_custom_data():
    request.kdict = settings()
    cookie_value = request.get_cookie('access_token')
    if cookie_value:
        try:
            SECRET_KEY = os.environ.get("SECRET_KEY")
            decoded_payload = jwt.decode(cookie_value, SECRET_KEY, algorithms=["HS256"])
            request.user = decoded_payload
        except ExpiredSignatureError:
            print("Token has expired.")
        except InvalidTokenError:
            print("Invalid token or signature.")
    else:
        request.user = None

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./static')

import socket    
host = socket.getfqdn()    
addr = socket.gethostbyname(host)
if(addr == '127.0.1.1'):
    app.run(host='localhost', port=8000, debug=True, reloader=True)