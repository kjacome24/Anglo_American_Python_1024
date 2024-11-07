from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación

app = Flask(__name__)  # Crea una nueva instancia de la clase Flask llamada "app"

# Ruta de inicio o página principal
@app.route('/')
def home():
    return "<h1>¡Bienvenido a la Galaxia de Star Wars!</h1><p>Explora las rutas para interactuar con personajes, citas y más.</p>"

# Ruta para mostrar un saludo Jedi famoso
@app.route('/jedi_saludo')
def jedi_saludo():
    return 'Que la Fuerza te acompañe!'

# Ruta para el Lado Oscuro
@app.route('/lado_oscuro')
def lado_oscuro():
    return 'Bienvenido al Lado Oscuro... Tenemos galletas.'

# Retornar un elemento HTML con descripción de una nave espacial
@app.route('/nave_espacial')
def nave_espacial():
    return "<h1>Halcón Milenario</h1><p>La nave más rápida de la galaxia, pilotada por Han Solo y Chewbacca.</p>"

# Ruta de contacto (para la sede de la Alianza Rebelde)
@app.route('/contacto/alianza_rebelde')
def contacto_rebelde():
    return "<h1>Cuartel General de la Alianza Rebelde</h1><p>Contacto: +56 9 1138 042</p>"

# Ruta para saludar a un Jedi por nombre
@app.route('/saludar_jedi/<nombre>')  
def saludar_jedi(nombre):
    return f'Hola, Jedi {nombre}. La Fuerza es fuerte contigo.'

# Ruta para saludar a un usuario con información completa y rol en la galaxia de Star Wars
@app.route('/hola/<nombre>/<rol>/<int:edad>')
def hola(nombre, rol, edad):
    return f"<h1>¡Bienvenido, {nombre}!</h1><p>Rol: {rol}, Edad: {edad}</p><p>Usa tus poderes sabiamente en la galaxia.</p>"

# Ruta para repetir una cita de Star Wars una cantidad específica de veces
@app.route('/cita/<cita>/<int:veces>')
def repetir_cita(cita, veces):
    return (f"<p>{cita}</p>") * veces

# Ruta para saludar con "Que la Fuerza te acompañe" repetido varias veces
@app.route('/saludo_fuerza/<nombre>/<int:num>')
def saludo_fuerza(nombre, num):
    return (f'<p>¡Que la Fuerza te acompañe, {nombre}!</p>') * num

# Ejemplo de ruta que devuelve una imagen
@app.route('/imagen_yoda')
def imagen_yoda():
    return '<h1>Maestro Yoda</h1><img src="https://starwars-visualguide.com/assets/img/characters/20.jpg" alt="Imagen del Maestro Yoda">'

# Iniciar la aplicación Flask en modo de depuración
if __name__ == "__main__":
    app.run(debug=True)
