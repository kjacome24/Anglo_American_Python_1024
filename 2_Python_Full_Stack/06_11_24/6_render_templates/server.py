from flask import Flask, render_template  # Importamos la clase Flask y la función render_template

app = Flask(__name__)  # Creamos una nueva instancia de la clase Flask llamada "app"


@app.route('/')
def bienvenido():
   # Renderizamos la plantilla 'index.html' para la ruta '/bienvenido'
   return render_template('index.html')


# Ejemplo de renderizado de plantilla con datos de usuario
@app.route('/user/<nombre>/<apellido>/<int:edad>')
def user(nombre, apellido, edad):
    # Enviamos los datos del usuario (nombre, apellido y edad) a la plantilla 'user.html'
    return render_template('user.html', nombre=nombre, apellido=apellido, edad=edad)


#### Usando Jinja con un tema de Star Wars
@app.route('/star_jinja')
def star_jinja():
    # Enviamos dos nuevos argumentos con un tema de Star Wars a la plantilla 'index2.html'
    return render_template('index2.html', cita="May the Force be with you", repite=3)


# Iniciar la aplicación Flask en modo de depuración
if __name__ == "__main__":
    app.run(debug=True)
