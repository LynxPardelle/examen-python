from flask import Flask, jsonify, request
from Models import db, Dispositivo
from logging import exception

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\dispositivo.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False
db.init_app(app)

# Routes
@app.route("/")
def home():
  return "<h1>Welcome</h1>"

@app.route("/api/dispositivos", methods=["GET"])
def getDispositivos():
  try:
    dispositivos = Dispositivo.query.all()
    toReturn = [dispositivo.serialize() for dispositivo in dispositivos]
    return jsonify(toReturn), 200 
  except Exception as e:
    exception("[SERVER]: Error")
    return jsonify({"message": "Ha ocurrido un error"}), 500

@app.route("/api/dispositivo", methods=["GET"])
def getDispositivoById():
  try:
    name = request.args["nombre_de_equipo"]
    dispositivo = Dispositivo.query.filter_by(nombre_de_equipo=name)
    if not dispositivo:
      return jsonify({"message": "No existe el dispositivo"}), 404
    else:
      return jsonify(dispositivo.serialize()), 200
  except Exception as e:
    exception("[SERVER]: Error")
    return jsonify({"message": "Ha ocurrido un error"}), 500

if __name__ == "__main__":
  app.run(debug = True, port=4666)