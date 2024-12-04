from flask import Flask, render_template, redirect, url_for  # Importamos la clase Flask y la función render_template

####Explain about the use of redirect and url_for####



##########Creacion de instancia##########
app = Flask(__name__) 

##########Rutas##########
@app.route('/')
def bienvenido():
   return redirect(url_for('juego'))

@app.route('/juego')
def juego():
    return render_template('juego.html')


@app.route('/juego/<int:number>')
def juego_x(number):
    return render_template('juego2.html', number = number)



@app.route('/juego/<int:number>/<color>')
def juego_y(number,color):
    return render_template('juego3.html', number = number, color = color)


#########bonus#########

# @app.route('/juego')
# def juego():
#     return render_template('juego3.html', number = 3 , color = 'red')


# @app.route('/juego/<int:number>')
# def juego_x(number):
#     return render_template('juego3.html', number = number, color = 'red')



# @app.route('/juego/<int:number>/<color>')
# def juego_y(number,color):
#     return render_template('juego3.html', number = number, color = color)


# Iniciar la aplicación Flask en modo de depuración
if __name__ == "__main__":
    app.run(debug=True)
