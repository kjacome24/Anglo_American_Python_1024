###Importacion de librerias
from flask import Flask, render_template, request, redirect, session
from usuarios import Usuario



######Creacion de la instacia de clase flask
app = Flask(__name__)




####rutas
@app.route('/')
def main():
    usuarios = Usuario.get_all()
    return render_template('index.html', usuarios = usuarios)


@app.route('/usuarios/nuevo')
def new():
    return render_template('new.html')

@app.route('/usuarios/crear', methods = ['POST'])
def crear_nuevo():
    data = {
        'nombre' : request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.crear(data)
    return redirect('/')


@app.route('/usuarios/<int:id>')
def usuario(id):
    data = {
        'id':id
    }
    usuario = Usuario.get_one(data)
    print(usuario)
    return render_template('usuario.html', usuario = usuario)

@app.route('/usuarios/editar/<int:id>')
def editar(id):
    data = {
        'id':id
    }
    usuario = Usuario.get_one(data)
    print(usuario)
    return render_template('usuario_edit.html', usuario = usuario)

@app.route('/usuarios/actualizar/<int:id>', methods = ['POST'])
def actualizar(id):
    data = {
        'id': id,
        'nombre' : request.form['nombre'],
        'apellido': request.form['apellido'],
        'email': request.form['email']
    }
    Usuario.actualizar(data)
    return redirect('/')



@app.route('/usuarios/eliminar/<int:id>')
def eliminar(id):
    data = {'id': id}
    Usuario.eliminar(data)
    return redirect('/')

###
if __name__=="__main__":
    app.run(debug=True)