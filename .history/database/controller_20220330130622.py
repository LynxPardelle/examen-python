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
          fecha_de_alta text,
          fecha_de_actualización text,
          potencia_actual interger,
          statusDispositivoId text
    )"""
  )
  cursor.commit()
  conn.close()


if __name__ == "__main__":
  createDB()
  createTable()