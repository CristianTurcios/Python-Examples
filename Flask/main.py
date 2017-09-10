from flask import Flask, request
from multiprocessing import Process
from Students import *
from Ingenieria import *

app = Flask(__name__)
server = Process(target=app.run)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/Students', methods=['GET'])
@app.route('/students', methods=['GET'])
@app.route('/Student', methods=['GET'])
@app.route('/student', methods=['GET'])
def hello():
    instance = Students('Cristian', 'Turcios', 'UNAH')
    return instance.getAllDataOfStudent()

@app.route('/Ingenieria')
@app.route('/ingenieria' , methods=['GET'])
def IngenieriaTest():
    ing = Ingenieria('Cristian', 'Turcios', 'UNAH')
    return ing.printFullNameUpperCase()

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        print func
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST', 'GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
