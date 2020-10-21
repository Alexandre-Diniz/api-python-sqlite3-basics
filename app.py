from flask import Flask, request, jsonify
import database

app = Flask(__name__)
app.config["DEBUG"] = False

@app.route('/', methods=['GET'])
def home():
    return "<h1>Home Page</h1>"

@app.route('/api/v1/', methods=['POST'])
def names():
    try:
        if 'id' in request.args and 'name' in request.args and 'begin_date' in request.args and 'end_date' in request.args:
            data = {}
            for key in request.args:
                data[key]=request.args[key]
            database.insert_in_table((int(data['id']),data['name'],data['begin_date'],data['end_date']))
            return '<h1>Done</h1>'
        else:
            return jsonify([])
    except:
        return jsonify([])

@app.route('/api/v1/', methods=['GET'])
def names_get():
    try:
        if 'id' in request.args:
            return jsonify(database.search_in_table_by_id(int(request.args['id'])))
        else:
            return '<h1>ID não fornecido</h1>'
    except:
        return '<h1>Erro</h1>'

@app.route('/api/v1/all', methods=['GET'])
def names_get_all():
    try:
        
        return jsonify(database.search_in_table_all())
    except:
        return '<h1>Erro get all</h1>'


app.run(port=8000)