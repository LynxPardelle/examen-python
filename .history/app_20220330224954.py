from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database\\dispositivo.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

class DispositivoSchema(ma.Schema):
  class Meta:
    fields = ('id', "nombre de equipo", "tipodispositivoId", "fecha de alta", "fecha de actualización", "potencia actual", "statusDispositivoId")

dispositivo_schema = DispositivoSchema()
dispositivos_schema = DispositivoSchema(many=True)

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