from bottle import Bottle, template, request

app = Bottle()
kdict = {}

@app.route('/')
def index():
    global kdict
    kdict = request.kdict
    kdict['pageTitle'] = 'ទំព័រ​​គ្រប់គ្រង'
    return template('admin/index', data=kdict)