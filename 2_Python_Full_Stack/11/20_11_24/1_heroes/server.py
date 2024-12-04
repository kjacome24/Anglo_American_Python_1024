#####Importacion de librerias
from flask import Flask, render_template, request, redirect 
from heroes import Heroe


#####Creacion de la instancia de la clase flask
app = Flask(__name__)


####rutas

@app.route('/')
def main():
    heroes = Heroe.get_all()
    print(heroes)
    return render_template('index.html', heroes = heroes)

@app.route('/heroes/nuevo')
def crear_nuevo():
    return render_template('nuevo.html')

@app.route('/heroes/crear', methods = ['POST'])
def nuevo():
    data = {
        'nombre' : request.form['nombre'],
        'poder' : request.form['poder'],
        'link_img' : request.form['link_img'],
        'bio': request.form['bio'],
    }
    Heroe.crear(data)
    return redirect('/')

@app.route('/heroes/eliminar/<int:id>')
def eliminar(id):
    data = {'id': id}
    Heroe.eliminar(data)
    return redirect('/')

@app.route('/heroes/ver/<int:id>')
def ver(id):
    data = {'id': id}
    heroe = Heroe.ver(data)
    print(heroe)
    return render_template('view_super.html',heroe = heroe)

@app.route('/heroes/editar/<int:id>')
def editar(id):
    data = {'id' : id}
    heroe = Heroe.ver(data)
    return render_template('editar.html',heroe = heroe)

@app.route('/heroes/editar_form/<int:id>', methods = ['POST'])
def editar_form(id):
    data = {'id' : id,
        'nombre' : request.form['nombre'],
        'poder' : request.form['poder'],
        'link_img' : request.form['link_img'],
        'bio': request.form['bio']
            }
    heroe = Heroe.editar(data)
    print(heroe)
    return redirect('/')

#####activar modo debug
if __name__=="__main__":
    app.run(debug=True)