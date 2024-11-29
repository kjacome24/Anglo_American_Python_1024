from flask_app import app
from flask import render_template, redirect,request,session
from flask_app.models.usuario import Usuario

@app.route('/pilotos/crear', methods = ['POST'])
def crear_usuario():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email']
    }

    if not Usuario.validar_usuario(data):

        return redirect('/')

    Usuario.save(data)
    return redirect('/')