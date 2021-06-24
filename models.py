from sqlalchemy.sql.sqltypes import DateTime
import db
from sqlalchemy import Column, Integer, String, Boolean
from datetime import datetime

'''
Creamos una clase llamada Tarea
Esta clase va a ser nuestro modelo de datos de la tarea (el cual nos servirá
luego para la base de datos)
Esta clase va a almacenar toda la información referente a una tarea
'''
class Tarea(db.Base):
    __tablename__ = "tarea"
    id = Column(Integer, primary_key=True) # Identificador único de cada tarea (primary key)
    contenido = Column(String(200), nullable=False) # Contenido de la tarea, un texto de máximo 200 caracteres
    categoria = Column(String(200), nullable=False) # Categboria de la tarea, un texto de máximo 200 caracteres
    fecha_limite = Column(DateTime, nullable=True)  # Fecha de la tarea, en formato DateTime
    hecha = Column(Boolean) # Booleano que indica si una tarea ha sido hecha o no
    editable = Column(Boolean) # Booleano que indica si una tarea se encuentra en estado de edicion o no

    def __init__(self, contenido, categoria, fecha_limite, hecha, editable):
        self.contenido = contenido
        self.categoria = categoria
        self.set_fecha(fecha_limite)
        self.hecha = hecha
        self.editable = editable

    def update(self, contenido, categoria, fecha_limite):
        self.contenido = contenido
        self.categoria = categoria
        self.set_fecha(fecha_limite)
        self.editable = False

    def set_fecha(self, fecha): # Introducir la fecha en la base de datos, es un proceso delicado, ya que hay que convertir un string a objeto datetime.
        try:                    # Si ocurre algun error, introducimos la fecha de hoy
            self.fecha_limite = datetime.strptime(fecha, r'%d/%m/%Y')
        except Exception as e:
            self.fecha_limite = datetime(1,1,1,0,0)

    def parsed_datetime(self):
        return self.fecha_limite.strftime(r'%d/%m/%Y')

    def __repr__(self):
        return "Tarea {}: {} {} {}({} {})".format(self.id, self.contenido, self.categoria, self.fecha_limite , self.hecha, self.editable)

    def __str__(self):
        return "Tarea {}: {} {} {}({} {})".format(self.id, self.contenido, self.categoria, self.fecha_limite, self.hecha, self.editable)