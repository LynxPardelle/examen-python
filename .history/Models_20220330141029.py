from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre_de_equipo = db.Column(db.String(200))
  tipodispositivoId = db.Column(db.Integer)
  fecha_de_alta = db.Column(db.String(200))
  fecha_de_actualización = db.Column(db.String(200))
  potencia_actual = db.Column(db.Integer)
  statusDispositivoId = db.Column(db.Integer)

  def __str__(self):
    return "\nnombre_de_equipo: {}. \ntipodispositivoId: {}. \nfecha_de_alta: {}. \nfecha_de_actualización: {}. \npotencia_actual: {}. \nstatusDispositivoId: {}\n".format(
      self.nombre_de_equipo,
      self.tipodispositivoId,
      self.fecha_de_alta,
      self.fecha_de_actualización,
      self.potencia_actual,
      self.statusDispositivoId
    )

class tiposdispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nombre_de_tipo = db.Column(db.String(200))

class StatusDispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  Descripcion = db.Column(db.String(200))

class lecturas(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  iddispositivo = db.Column(db.Integer)
  idtipodispositivo = db.Column(db.Integer)
  potenciaActual = db.Column(db.Integer)
  timestamp = db.Column(db.String(200))
  tipodispositivoId = db.Column(db.Integer)
  fecha_alta = db.Column(db.String(200))
  fecha_de_actualización = db.Column(db.String(200))
  potencia_actual = db.Column(db.Integer)
  statusDispositivoId = db.Column(db.Integer)

class Mantenimientos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  dispositivoId = db.Column(db.Integer)
  fecha_ingreso = db.Column(db.String(200))

