from flask import Flask
from Models import db, Dispositivo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///database\\dispositivo.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False
db.init_app(app)

# Routes
@app.route("/")
def home():
  return "<h1>Welcome</h1>"

@app.route("/api/dispositivos")
def getDispositivos():
  dispositivos = Dispositivo.query.all()
  print(dispositivos)
  return "<h1>Success</h1>"

if __name__ == "__main__":
  app.run(debug = True, port=4666)