from flask import Flask
from Models import db, Dispositivo

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///database\\dispositivo.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False

@app.route("/")
def home():
  return "<h1>Welcome</h1>"

if __name__ == "__main__":
  app.run(debug = True, port=4666)