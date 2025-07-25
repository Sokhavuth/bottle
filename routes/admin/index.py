from bottle import Bottle, template, request, redirect

app = Bottle()
kdict = {}

@app.route('/')
def index():
    if(not request.user):
        redirect('/login')
    else:
        global kdict
        kdict = request.kdict
        kdict['pageTitle'] = 'ទំព័រ​​គ្រប់គ្រង'
        kdict['user'] = request.user
        return template('admin/index', data=kdict)