from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\dispositivo.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False


db = SQLAlchemy(app)
ma = Marshmallow(app)

class Dispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  nombre_de_equipo = db.Column(db.String(200))
  tipodispositivoId = db.Column(db.Integer)
  fecha_de_alta = db.Column(db.String(200))
  fecha_de_actualización = db.Column(db.String(200))
  potencia_actual = db.Column(db.Integer)
  statusDispositivoId = db.Column(db.Integer)

  def __init__(self, nombre_de_equipo, tipodispositivoId, fecha_de_alta, fecha_de_actualización, potencia_actual, statusDispositivoId):
    self.nombre_de_equipo = nombre_de_equipo
    self.tipodispositivoId = tipodispositivoId
    self.fecha_de_alta = fecha_de_alta
    self.fecha_de_actualización = fecha_de_actualización
    self.potencia_actual = potencia_actual
    self.statusDispositivoId = statusDispositivoId

  def __str__(self):
    return "\nid: {}. \nnombre_de_equipo: {}. \ntipodispositivoId: {}. \nfecha_de_alta: {}. \nfecha_de_actualización: {}. \npotencia_actual: {}. \nstatusDispositivoId: {}\n".format(
      self.id,
      self.nombre_de_equipo,
      self.tipodispositivoId,
      self.fecha_de_alta,
      self.fecha_de_actualización,
      self.potencia_actual,
      self.statusDispositivoId
    )

  def serialize(self):
    return {
      "id": self.id,
      "nombre de equipo": self.nombre_de_equipo,
      "tipodispositivoId": self.tipodispositivoId,
      "fecha de alta": self.fecha_de_alta,
      "fecha de actualización": self.fecha_de_actualización,
      "potencia actual": self.potencia_actual,
      "statusDispositivoId": self.statusDispositivoId
    }

class DispositivoSchema(ma.Schema):
  class Meta:
    fields = ('id', "nombre de equipo", "tipodispositivoId", "fecha de alta", "fecha de actualización", "potencia actual", "statusDispositivoId")

dispositivo_schema = DispositivoSchema()
dispositivos_schema = DispositivoSchema(many=True)

class tiposdispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  nombre_de_tipo = db.Column(db.String(200), unique = True)

  def __init__(self, nombre_de_tipo):
    self.nombre_de_tipo = nombre_de_tipo

  def __str__(self):
    return "\nid: {}. \nnombre_de_tipo: {}\n".format(
      self.id,
      self.nombre_de_tipo,
    )

  def serialize(self):
    return {
      "id": self.id,
      "nombre de tipo": self.nombre_de_tipo,
    }

class StatusDispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  Descripcion = db.Column(db.String(200))

  def __init__(self, Descripcion):
    self.Descripcion = Descripcion

  def __str__(self):
    return "\nid: {}. \nDescripcion: {}\n".format(
      self.id,
      self.Descripcion,
    )

  def serialize(self):
    return {
      "id": self.id,
      "Descripcion": self.Descripcion,
    }

class lecturas(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  iddispositivo = db.Column(db.Integer)
  idtipodispositivo = db.Column(db.Integer)
  potenciaActual = db.Column(db.Integer)
  timestamp = db.Column(db.String(200))
  
  def __init__(self, iddispositivo, idtipodispositivo, potenciaActual, timestamp):
    self.iddispositivo = iddispositivo
    self.idtipodispositivo = idtipodispositivo
    self.potenciaActual = potenciaActual
    self.timestamp = timestamp

  def __str__(self):
    return "\nid: {}. \niddispositivo: {}. \nidtipodispositivo: {}. \npotenciaActual: {}. \ntimestamp: {}\n".format(
      self.id,
      self.iddispositivo,
      self.idtipodispositivo,
      self.potenciaActual,
      self.timestamp,
    )

  def serialize(self):
    return {
      "id": self.id,
      "iddispositivo": self.iddispositivo,
      "idtipodispositivo": self.idtipodispositivo,
      "potenciaActual": self.potenciaActual,
      "timestamp": self.timestamp,
    }

class Mantenimientos(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  dispositivoId = db.Column(db.Integer)
  fecha_ingreso = db.Column(db.String(200))
  
  def __init__(self, dispositivoId, fecha_ingreso):
    self.dispositivoId = dispositivoId
    self.fecha_ingreso = fecha_ingreso
  def __str__(self):
    return "\nid: {}. \ndispositivoId: {}. \nfecha_ingreso: {}\n".format(
      self.id,
      self.dispositivoId,
      self.fecha_ingreso
    )

  def serialize(self):
    return {
      "id": self.id,
      "dispositivoId": self.dispositivoId,
      "fecha_ingreso": self.fecha_ingreso,
    }

db.create_all()

# Routes
@app.route("/")
def home():
  return "<h1>Welcome</h1>"

# POST
@app.route("/api/dispositivo", methods=["POST", "GET", "PUT", "DELETE"])
def createDispositivo():
  try:
    def POST():
      if request.json:
        reqJSON = request.json
        posibleValues = ["nombre_de_equipo", "tipodispositivoId", "fecha_de_alta", "fecha_de_actualización", "potencia_actual", "statusDispositivoId"]
        newDisp = {}
        for value in reqJSON:
          if value in posibleValues: 
            newDisp[value] = reqJSON[value]
        newDispositivo = Dispositivo(**newDisp)  
        db.session.add(newDispositivo)
        db.session.commit()
        return jsonify(newDispositivo.serialize())

    def GET():
      if request.args and request.args['id']:
        dispositivo = Dispositivo.query.get(request.args['id'])
        if not dispositivo:
          return jsonify({"message": "No existe el dispositivo"}), 404
        else:
          return jsonify(dispositivo.serialize()), 200
      else:
        return jsonify({"message": "No existe el dispositivo"}), 404
  
    switch = {
      'POST': POST(),
      'GET': GET(),
      # 'PUT': PUT(),
      # 'DELETE': DELETE(),
    }

    return switch.get(request.method)
  except Exception as e:
    exception("[SERVER]: Error")
    exception(e)
    return jsonify('{"message": "Ha ocurrido un error"}'), 500

# GET
@app.route("/api/dispositivos", methods=["GET"])
def getDispositivos():
  try:
    dispositivos = Dispositivo.query.all()
    toReturn = [dispositivo.serialize() for dispositivo in dispositivos]
    return jsonify(toReturn), 200 
  except Exception as e:
    exception("[SERVER]: Error")
    return jsonify({"message": "Ha ocurrido un error", "error": e}), 500

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
    return jsonify({"message": "Ha ocurrido un error", "error": e}), 500

@app.route("/api/find-dispositivo", methods=["GET"])
def findDispositivo():
  try:
    fields = {}
    for arg in request.args:
      if arg == "id" or arg == "nombre_de_equipo" or arg == "tipodispositivoId" or arg == "fecha_de_alta" or arg == "fecha_de_actualización" or arg == "potencia_actual" or arg == "statusDispositivoId":
        fields[arg] = request.args[arg]
    dispositivo = Dispositivo.query.filter_by(**fields).first()
    if not dispositivo:
      return jsonify({"message": "No existe el dispositivo", "error": e}), 404
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
    return jsonify({"message": "Ha ocurrido un error", "error": e}), 500

# PUT

# DELETE



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