from flask import Flask
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

@app.route("/api/dispositivos")
def getDispositivos():
  try:
    dispositivos = Dispositivo.query.all()
    toReturn = [Dispositivo.serialize() for dispositivo in dispositivos]
    #""" for dispositivo in dispositivos:
    #  print(dispositivo) """
    return "<h1>Success</h1>"  
  except Exception as e:
    print("[SERVER]: Error")
    return "<h1>Error</h1>"  

if __name__ == "__main__":
  app.run(debug = True, port=4666)