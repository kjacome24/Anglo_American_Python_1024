from flask import Flask, render_template, redirect, request, session

#######cracion de instancia de flask
app = Flask(__name__)

app.secret_key = '123445678'


################rutas
@app.route('/')
def main():
    return render_template('index.html')

######Iniciamos flask en modo debug
if __name__== "__main__":
    app.run(debug=True)


