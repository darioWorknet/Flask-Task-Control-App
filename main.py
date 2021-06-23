from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__) # En app se encuentra nuestro servidor

# La barra (el slash) se conoce como la página de inicio (página home).
@app.route('/')
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    return render_template("index.html", lista_de_tareas=todas_las_tareas)


@app.route('/crear-tarea', methods=['POST'])
def crear():
    tarea = Tarea(contenido=request.form['contenido_tarea'], 
                categoria=request.form['categoria_tarea'],
                fecha_limite=request.form['fecha_limite_tarea'], # Parseado a Datetime mas adelante
                hecha=False,
                editable=False) # id no es necesario asignarlo (primary key)
    db.session.add(tarea) # Añadir el objeto de Tarea a la base de datos
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return  redirect(url_for('home'))


@app.route('/eliminar-tarea/<id>')
def eliminar(id):
    db.session.query(Tarea).filter_by(id=int(id)).delete() # Se busca dentro de la base de datos, aquel registro cuyo id coincida con el aportado por el parametro de la ruta. Cuando se encuentra se elimina
    db.session.commit() # Ejecutar la operación pendiente de la base de datos
    return redirect(url_for('home')) # Esto nos redirecciona a la función home() y si todo ha ido bien, al refrescar, la tarea eliminada ya no aparecera en el listado


@app.route('/editar-tarea/<id>')
def editar(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.editable = True
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/commit-tarea/<id>', methods=['POST'])
def commit(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    # tarea.contenido = request.form['contenido_tarea']
    # tarea.categoria = request.form['categoria_tarea']
    # tarea.fecha_limite = request.form['fecha_limite_tarea']
    # tarea.editable=False
    tarea.update(request.form['contenido_tarea'], request.form['categoria_tarea'], request.form['fecha_limite_tarea'])
    db.session.commit()
    return  redirect(url_for('home'))


@app.route('/tarea-hecha/<id>')
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id=int(id)).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == '__main__':
    db.Base.metadata.create_all(db.engine) # Creamos el modelo de datos
    app.run(debug=True)