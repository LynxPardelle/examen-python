import sqlite3 as sql

DB_PATH = "../DBS/dispositivo.db"

def createDB():
  conn = sql.connect(DB_PATH)
  conn.commit()
  conn.close()

if __name__ == "__main__":
  createDB()