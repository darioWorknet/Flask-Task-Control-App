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
    id = Column(Integer, primary_key=True) # Identificador único de cada tarea (no puede haber dos tareas con el mismo id, por eso es primary key)
    contenido = Column(String(200), nullable=False) # Contenido de la tarea, un texto de máximo 200 caracteres
    categoria = Column(String(200), nullable=False)
    fecha_limite = Column(DateTime, nullable=True)
    hecha = Column(Boolean) # Booleano que indica si una tarea ha sido hecha o no
    editable = Column(Boolean)
    def __init__(self, contenido, categoria, fecha_limite, hecha, editable):
        # Recordemos que el id no es necesario crearlo manualmente, lo añade la base de datos automaticamente
        self.contenido = contenido
        self.categoria = categoria
        self.fecha_limite = datetime.strptime(fecha_limite, r'%d/%m/%y')
        self.hecha = hecha
        self.editable = editable
    def update(self, contenido, categoria, fecha_limite):
        self.contenido = contenido
        self.categoria = categoria
        self.fecha_limite = datetime.strptime(fecha_limite, r'%d/%m/%y')
        self.editable = False
    def parsed_datetime(self):
        return self.fecha_limite.strftime(r'%d/%m/%y')
    def __repr__(self):
        return "Tarea {}: {} {} {}({} {})".format(self.id, self.contenido, self.categoria, self.fecha_limite , self.hecha, self.editable)
    def __str__(self):
        return "Tarea {}: {} {} {}({} {})".format(self.id, self.contenido, self.categoria, self.fecha_limite, self.hecha, self.editable)