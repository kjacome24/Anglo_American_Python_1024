from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)

app.secret_key = 'Esta es tu clave secreta!' #Establecemos una clave secreta


# La ruta raíz renderizará nuestro formulario
@app.route('/')
def index():
   return render_template("index.html")


@app.route('/mostrar_usuario')
def mostrar_usuario():
    print("Usuario redirigido")
    nombre = session['nombre_usuario']
    email = session['email_usuario']
    return render_template("mostrar.html", nombre=nombre, email=email)


@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    print("Ricibiendo info....")
    print(request.form)
    session['nombre_usuario'] = request.form['nombre']
    session['email_usuario'] = request.form['email']
    return redirect('/mostrar_usuario')


if __name__ == "__main__":

   app.run(debug=True)