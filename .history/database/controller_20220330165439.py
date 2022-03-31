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
          id integer,
          nombre_de_equipo text,
          tipodispositivoId text,
          fecha_de_alta text,
          fecha_de_actualización text,
          potencia_actual integer,
          statusDispositivoId text
    )"""
  )
  conn.commit()
  conn.close()

# def addValues():
#   conn = sql.connect(DB_PATH)
#   cursor = conn.cursor()
#   data = [
#     (1, "1", "Celda", "1/1/2021", "2/2/2021", 1, "en mantenimiento"),
#     (2, "2", "aerogenerador", "1/1/2021", "2/2/2021", 1, "En operación"),
#     (3, "3", "turbina hidroeléctrica", "1/1/2021", "2/2/2021", 1, "en mantenimiento"),
#     (4, "4", "Celda", "1/1/2021", "2/2/2021", 1, "En operación"),
#   ]
#   cursor.executemany("""INSERT INTO dispositivo VALUES (?, ?, ?, ?, ?, ?, ?)""", data)
#   conn.commit()
#   conn.close()

if __name__ == "__main__":
  createDB()
  createTable()
  # addValues()