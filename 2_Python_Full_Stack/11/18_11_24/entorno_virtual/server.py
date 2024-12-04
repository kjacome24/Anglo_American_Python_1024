###Importacion de librerias
from flask import Flask, render_template, request, redirect, session
from personajes import Personaje
from naves import Nave




######Creacion de la instacia de clase flask
app = Flask(__name__)




####rutas
@app.route('/')
def main():
    personajes = Personaje.get_all()
    naves = Nave.get_all()

    return render_template('index.html', personajesx = personajes, navesx = naves)

@app.route('/naves/<int:id>')
def nave(id):
    data = {
        'id':id
    }
    nave = Nave.get_one(data)
    print(nave)
    return render_template('nave.html', navex = nave)

###
if __name__=="__main__":
    app.run(debug=True)