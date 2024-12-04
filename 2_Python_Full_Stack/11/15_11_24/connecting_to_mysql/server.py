from flask import Flask, render_template,session
from personajes import Personaje

#####Creacion de la instancia de clase Flask
app = Flask(__name__)

app.secret_key = '12345'

#####Rutas
@app.route('/')
def main():
    # personajes = Personaje.get_all()
    # print(personajes)
    return render_template('index.html')


@app.route('/personajes')
def personajes():
    personajes = Personaje.get_all()
    return render_template('personajes.html',personajes = personajes)

###Incionaciacion de metodo debug de flask 
if __name__=="__main__":
    app.run(debug=True)
