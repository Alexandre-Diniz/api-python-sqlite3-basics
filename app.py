from flask import Flask, request, jsonify
from database import DataBase

app = Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
    return "<h1>Home Page</h1>"

@app.route('/api/v1/', methods=['POST'])
def names():
    try:
        db = DataBase()
        if 'id' in request.args and 'name' in request.args and 'begin_date' in request.args and 'end_date' in request.args:
            data = {}
            for key in request.args:
                data[key]=request.args[key]
            db.insert_one((int(data['id']),data['name'],data['begin_date'],data['end_date']))
            return '<h1>Done in insert one</h1>'
        else:
            return jsonify([])
    except:
        return jsonify([])

@app.route('/api/v1/', methods=['GET'])
def names_get():
    try:
        db = DataBase()
        if 'id' in request.args:
            return jsonify(db.find_by_id(int(request.args['id'])))
        else:
            return '<h1>ID não fornecido</h1>'
    except:
        return '<h1>Erro in find by id</h1>'

@app.route('/api/v1/all', methods=['GET'])
def names_get_all():
    try:
        db = DataBase()
        return jsonify(db.search_in_table_all())
    except:
        return '<h1>Erro get all</h1>'


app.run(port=8000)