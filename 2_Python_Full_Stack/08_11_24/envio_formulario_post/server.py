from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# La ruta raíz renderizará nuestro formulario
@app.route('/')
def index():
   return render_template("index.html")


@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
   print("Ricibiendo info....")
   print(request.form)
   return redirect('/')


if __name__ == "__main__":

   app.run(debug=True)