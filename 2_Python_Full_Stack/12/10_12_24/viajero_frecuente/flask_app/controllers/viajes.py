from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.viaje import Viaje


@app.route('/dashboard')
def dashboard():
    if session.get('id') == None:
        return redirect('/')
    viajes = Viaje.viajes_con_usuario()
    return render_template('dashboard.html', viajes = viajes )

@app.route('/ver/<int:id>')
def ver_viaje(id):
    data = {'id': id}
    viaje = Viaje.viaje_con_unidos(data)
    unido = False
    for resultado in viaje.unirse:
        if session['id'] == resultado.id:
            unido = True
            break
    return render_template('viaje.html',viaje = viaje, unido = unido)

@app.route('/salirse', methods = ['POST'])
def salirse():
    data = {
        "usuario_id" : request.form['usuario_id'],
        "viaje_id" : request.form['viaje_id']
    }
    Viaje.salirse(data)
    return redirect(f"/ver/{data['viaje_id']}")

@app.route('/unirse', methods = ['POST'])
def unirse():
    data = {
        "usuario_id" : request.form['usuario_id'],
        "viaje_id" : request.form['viaje_id']
    }
    Viaje.unirse(data)
    return redirect(f"/ver/{data['viaje_id']}")

@app.route('/borrar/<int:id>')
def borrar(id):
    data = {'id': id}
    Viaje.borrar_unirse(data)
    Viaje.borrar_viajes(data)
    return redirect('/dashboard')