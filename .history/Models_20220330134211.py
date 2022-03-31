from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dispositivo(db.Model):
  id = db.Column(db.Interger, primary_key=True)
  nombre_de_equipo = db.Column(db.String(200))
  tipodispositivoId = db.Column(db.Interger)
  fecha_alta = db.Column(db.String(200))
  fecha_de_actualización = db.Column(db.String(200))
  potencia_actual = db.Column(db.Interger)
  statusDispositivoId = db.Column(db.Interger)

class tiposdispositivo(db.Model):
  id = db.Column(db.Interger, primary_key=True)
  nombre_de_tipo = db.Column(db.String(200))

class StatusDispositivo(db.Model):
  id = db.Column(db.Interger, primary_key=True)
  Descripcion = db.Column(db.String(200))

class lecturas(db.Model):
  id = db.Column(db.Interger, primary_key=True)
  iddispositivo = db.Column(db.Interger)
  idtipodispositivo = db.Column(db.Interger)
  potenciaActual = db.Column(db.Interger)
  timestamp = db.Column(db.String(200))
  tipodispositivoId = db.Column(db.Interger)
  fecha_alta = db.Column(db.String(200))
  fecha_de_actualización = db.Column(db.String(200))
  potencia_actual = db.Column(db.Interger)
  statusDispositivoId = db.Column(db.Interger)


