from bottle import Bottle, template, request, redirect
from db.user import userDB
import bcrypt
import json

app = Bottle()
kdict = {}

@app.route('/')
def index():
    #userDB.createRootUser()
    global kdict
    kdict = request.kdict
    kdict['pageTitle'] = 'ទំព័រ​​ចុះ​ឈ្មោះ'
    return template('login', data=kdict)

@app.route('/', method='POST')
def index_post():
    global kdict
    email = request.forms.get('email')
    result = userDB.checkUser(email)
    
    rows = result.all()
    if(rows != []):
        password = request.forms.get('password')
        plain_password_attempt = password.encode('UTF-8')
        user = rows[0]
        password = user[3]
        hashed_password = password.encode('UTF-8')
        if bcrypt.checkpw(plain_password_attempt, hashed_password):
            #session['user'] = json.dumps({'id':user[0], 'name':user[1], 'role':user[4]})
            redirect('/admin')
        else:
            kdict['message'] = 'Email ឬ​ពាក្យ​សំងាត់​មិន​ត្រឹមត្រូវ​ទេ!'
            return template('login', data=kdict)
        
    else:
        kdict['message'] = 'Email ឬ​ពាក្យ​សំងាត់​មិន​ត្រឹមត្រូវ​ទេ!'
        return template('login', data=kdict)