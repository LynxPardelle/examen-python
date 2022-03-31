import sqlite3 as sql

DB_PATH = "dispositivo.db"

def createDB():
  conn = sql.connect(DB_PATH)
  conn.commit()
  conn.close()

def createTable():
  conn = sql.connect(DB_PATH)
  cursor = conn.cursor()
  cursor.execute(
    """CREATE TABLE dispositivo (
          id interger,
          nombre de equipo text,
          tipodispositivoId text,
          fecha de alta text,
          fecha de actualización text,
          potencia actual interger,
          statusDispositivoId text
    )"""
  )
  cursor.commit()
  conn.close()


if __name__ == "__main__":
  createDB()
  createTable()