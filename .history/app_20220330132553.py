from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URL"] = "sqlite:///database\\dispositivo.db"
app.config["SQLALCHEMY_TRAK_MODIFICATIONS"] = False

if __name__ == "__main__":
  app.run(debug = True, port=666)