from flask import Flask, jsonify, request
from Models import db, Dispositivo, tiposdispositivo, StatusDispositivo, lecturas, Mantenimientos
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\dispositivo.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False

# Routes
@app.route("/")
def home():
  return "<h1>Welcome</h1>"

# GET
@app.route("/api/dispositivos", methods=["GET"])
def getDispositivos():
  try:
    dispositivos = Dispositivo.query.all()
    toReturn = [dispositivo.serialize() for dispositivo in dispositivos]
    return jsonify(toReturn), 200 
  except Exception as e:
    exception("[SERVER]: Error")
    return jsonify({"message": "Ha ocurrido un error"}), 500

@app.route("/api/dispositivo/<id>", methods=["GET"])
def getDispositivoById(id):
  try:
    dispositivo = Dispositivo.query.get(id)
    if not dispositivo:
      return jsonify({"message": "No existe el dispositivo"}), 404
    else:
      return jsonify(dispositivo.serialize()), 200
  except Exception as e:
    exception("[SERVER]: Error")
    return jsonify({"message": "Ha ocurrido un error"}), 500

@app.route("/api/find-dispositivo", methods=["GET"])
def findDispositivo():
  try:
    fields = {}
    for arg in request.args:
      if arg == "id" or arg == "nombre_de_equipo" or arg == "tipodispositivoId" or arg == "fecha_de_alta" or arg == "fecha_de_actualización" or arg == "potencia_actual" or arg == "statusDispositivoId":
        fields[arg] = request.args[arg]
    dispositivo = Dispositivo.query.filter_by(**fields).first()
    if not dispositivo:
      return jsonify({"message": "No existe el dispositivo"}), 404
    else:
      return jsonify(dispositivo.serialize()), 200
  except Exception as e:
    exception("[SERVER]: Error")
    return jsonify({"message": "Ha ocurrido un error"}), 500

@app.route("/api/find-dispositivos", methods=["GET"])
def findDispositivos():
  try:
    fields = {}
    for arg in request.args:
      if arg == "id" or arg == "nombre_de_equipo" or arg == "tipodispositivoId" or arg == "fecha_de_alta" or arg == "fecha_de_actualización" or arg == "potencia_actual" or arg == "statusDispositivoId":
        fields[arg] = request.args[arg]
    dispositivos = Dispositivo.query.filter_by(**fields)
    if not dispositivos:
      return jsonify({"message": "No existen dispositivo con ese filtro"}), 404
    else:
      toReturn = [dispositivo.serialize() for dispositivo in dispositivos]
      return jsonify(toReturn), 200 
  except Exception as e:
    exception("[SERVER]: Error")
    return jsonify({"message": "Ha ocurrido un error"}), 500

# POST
@app.route("/api/dispositivo", methods=["POST"])
def createDispositivo():
  reqJSON = request.json
  posibleValues = ["nombre_de_equipo", "tipodispositivoId", "fecha_de_alta", "fecha_de_actualización", "potencia_actual", "statusDispositivoId"]
  newDisp = {}
  for value in reqJSON:
    if value in posibleValues: 
      newDisp[value] = reqJSON[value]
  
  # newDisp["id"] = 1

  # dispositivos = Dispositivo.query.all()
  # print(dispositivos)
  # if dispositivos.size != 0:
  #   dispositivos = [dispositivo.serialize() for dispositivo in dispositivos]
  #   for dispositivo in dispositivos:
  #     if newDisp["id"] == dispositivo["id"]: newDisp["id"] + 1

  newDispositivo = Dispositivo(**newDisp)  
  db.session.add(newDispositivo)
  db.session.commit()

  print(newDispositivo)
  return jsonify(newDispositivo.serialize())

# CORS
@app.after_request
def after_request(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS, PUT, DELETE"
    response.headers["Access-Control-Allow-Headers"] = "Accept, Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization"
    return response

# Run
if __name__ == "__main__":
  app.run(debug = True, port=4666)