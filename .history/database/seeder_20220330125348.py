import sqlite3 as sql

DB_PATH = ""

def createDB():
  conn = sql.connect(DB_PATH)

if __name__ == "__main__":
  print("Hola")