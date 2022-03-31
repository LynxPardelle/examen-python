from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  nombre_de_equipo = db.Column(db.String(200))
  tipodispositivoId = db.Column(db.Integer)
  fecha_de_alta = db.Column(db.String(200))
  fecha_de_actualización = db.Column(db.String(200))
  potencia_actual = db.Column(db.Integer)
  statusDispositivoId = db.Column(db.Integer)

  def __init__(self, nombre_de_equipo, tipodispositivoId, fecha_de_alta, fecha_de_actualización, potencia_actual, statusDispositivoId):
    self.nombre_de_equipo = nombre_de_equipo
    self.tipodispositivoId = tipodispositivoId
    self.fecha_de_alta = fecha_de_alta
    self.fecha_de_actualización = fecha_de_actualización
    self.potencia_actual = potencia_actual
    self.statusDispositivoId = statusDispositivoId

  def __str__(self):
    return "\nid: {}. \nnombre_de_equipo: {}. \ntipodispositivoId: {}. \nfecha_de_alta: {}. \nfecha_de_actualización: {}. \npotencia_actual: {}. \nstatusDispositivoId: {}\n".format(
      self.id,
      self.nombre_de_equipo,
      self.tipodispositivoId,
      self.fecha_de_alta,
      self.fecha_de_actualización,
      self.potencia_actual,
      self.statusDispositivoId
    )

  def serialize(self):
    return {
      "id": self.id,
      "nombre de equipo": self.nombre_de_equipo,
      "tipodispositivoId": self.tipodispositivoId,
      "fecha de alta": self.fecha_de_alta,
      "fecha de actualización": self.fecha_de_actualización,
      "potencia actual": self.potencia_actual,
      "statusDispositivoId": self.statusDispositivoId
    }

class tiposdispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  nombre_de_tipo = db.Column(db.String(200), unique = True)

  def __init__(self, nombre_de_tipo):
    self.nombre_de_tipo = nombre_de_tipo

  def __str__(self):
    return "\nid: {}. \nnombre_de_tipo: {}\n".format(
      self.id,
      self.nombre_de_tipo,
    )

  def serialize(self):
    return {
      "id": self.id,
      "nombre de tipo": self.nombre_de_tipo,
    }

class StatusDispositivo(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  Descripcion = db.Column(db.String(200))

  def __init__(self, Descripcion):
    self.Descripcion = Descripcion

  def __str__(self):
    return "\nid: {}. \nDescripcion: {}\n".format(
      self.id,
      self.Descripcion,
    )

  def serialize(self):
    return {
      "id": self.id,
      "Descripcion": self.Descripcion,
    }

class lecturas(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  iddispositivo = db.Column(db.Integer)
  idtipodispositivo = db.Column(db.Integer)
  potenciaActual = db.Column(db.Integer)
  timestamp = db.Column(db.String(200))
  
  def __init__(self, iddispositivo, idtipodispositivo, potenciaActual, timestamp):
    self.iddispositivo = iddispositivo
    self.idtipodispositivo = idtipodispositivo
    self.potenciaActual = potenciaActual
    self.timestamp = timestamp

  def __str__(self):
    return "\nid: {}. \niddispositivo: {}. \nidtipodispositivo: {}. \npotenciaActual: {}. \ntimestamp: {}\n".format(
      self.id,
      self.iddispositivo,
      self.idtipodispositivo,
      self.potenciaActual,
      self.timestamp,
    )

  def serialize(self):
    return {
      "id": self.id,
      "iddispositivo": self.iddispositivo,
      "idtipodispositivo": self.idtipodispositivo,
      "potenciaActual": self.potenciaActual,
      "timestamp": self.timestamp,
    }

class Mantenimientos(db.Model):
  id = db.Column(db.Integer, primary_key=True, unique = True)
  dispositivoId = db.Column(db.Integer)
  fecha_ingreso = db.Column(db.String(200))
  
  def __init__(self, dispositivoId, fecha_ingreso):
    self.dispositivoId = dispositivoId
    self.fecha_ingreso = fecha_ingreso
  def __str__(self):
    return "\nid: {}. \ndispositivoId: {}. \nfecha_ingreso: {}\n".format(
      self.id,
      self.dispositivoId,
      self.fecha_ingreso
    )

  def serialize(self):
    return {
      "id": self.id,
      "dispositivoId": self.dispositivoId,
      "fecha_ingreso": self.fecha_ingreso,
    }
