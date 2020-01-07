from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from turbineDAO import turbineDAO

app = Flask(__name__, static_url_path='', static_folder='.')
CORS(app)

#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/turbines"
@app.route('/turbines')
def getAll():
    results = turbineDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/turbines/2"
@app.route('/turbines/<int:ID>')
def findByID(ID):
    foundTurbine = turbineDAO.findByID(ID)

    return jsonify(foundTurbine)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Model\":\"SG 2.6-114\",\"Manufacturer\":\"Siemens\",\"Rating\":2.6}" http://127.0.0.1:5000/turbines
@app.route('/turbines', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    turbine = {
        "Model": request.json['Model'],
        "Manufacturer": request.json['Manufacturer'],
        "Rating": request.json['Rating'],
    }
    values =(turbine['Model'],turbine['Manufacturer'],turbine['Rating'])
    newID = turbineDAO.create(values)
    turbine['ID'] = newID
    return jsonify(turbine)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Model\":\"E-70\",\"Manufacturer\":\"Enercon\",\"Rating\":1.9}" http://127.0.0.1:5000/turbines/1
@app.route('/turbines/<int:ID>', methods=['PUT'])
def update(ID):
    foundTurbine = turbineDAO.findByID(ID)
    if not foundTurbine:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Rating' in reqJson and type(reqJson['Rating']) is not int:
        abort(400)

    if 'Model' in reqJson:
        foundTurbine['Model'] = reqJson['Model']
    if 'Manufacturer' in reqJson:
        foundTurbine['Manufacturer'] = reqJson['Manufacturer']
    if 'Rating' in reqJson:
        foundTurbine['Rating'] = reqJson['Rating']
    values = (foundTurbine['Model'],foundTurbine['Manufacturer'],foundTurbine['Rating'],foundTurbine['ID'])
    turbineDAO.update(values)
    return jsonify(foundTurbine)
        

    

@app.route('/turbines/<int:ID>' , methods=['DELETE'])
def delete(ID):
    turbineDAO.delete(ID)
    return jsonify({"Done":True})




if __name__ == '__main__' :
    app.run(debug= True)