# Proyecto Flask - Configuración de Entorno Virtual y Proyecto

Este documento proporciona instrucciones paso a paso para configurar un entorno virtual con venv, instalar Flask y crear un proyecto básico en Flask.

## Crear un Entorno Virtual

Ejecuta el siguiente comando en la terminal para crear un entorno virtual llamado `FlaskVenv`:

```bash
python -m venv FlaskVenv
```

## Activar el Entorno Virtual

Activa el entorno virtual usando el comando correspondiente según el tipo de terminal en tu sistema operativo:

### Command Prompt:
```cmd
FlaskVenv\Scripts\activate
```
### PowerShell:
```powershell
.\FlaskVenv\Scripts\Activate
```

Una vez que el entorno virtual esté activado, verás `(FlaskVenv)` al inicio de la línea en la terminal, indicando que estás en el entorno virtual.

## Desactivar el Entorno Virtual

Cuando termines de usar el entorno virtual, puedes desactivarlo con el siguiente comando:

```bash
deactivate
```



## Instalar Flask

Con el entorno virtual activo, instala Flask usando el siguiente comando:

```bash
pip install flask
```

## Organizar el Proyecto

Con el entorno virtual activo, organiza tu proyecto creando una carpeta llamada `MyEnterprise`, donde almacenarás tu código:

```bash
mkdir MyEnterprise      # Creamos la carpeta MyEnterprise
cd MyEnterprise         # Entramos en la carpeta
pwd                     # Mostramos la ubicación actual
# /ruta/completa/del/proyecto/MyEnterprise/
```

## Crear el Archivo `server.py`

Dentro de la carpeta `MyEnterprise/`, crea un archivo llamado `server.py` y agrega el siguiente código para inicializar un servidor Flask y mostrar un mensaje simple en la ruta raíz:

```python
# Filename: server.py

from flask import Flask  # Importamos la clase Flask

app = Flask(__name__)    # Creamos una instancia de la clase Flask

@app.route('/')          # Decorador de ruta
def index():             # Función que se ejecuta cuando se accede a la ruta raíz
    return "<h1>Hola Mundo Flask!!</h1>"  # Devolvemos una cadena de texto

if __name__ == "__main__":  # Aseguramos que este archivo se ejecute directamente
    app.run(debug=True)     # Ejecutamos la aplicación en modo depuración
```

## Ejecutar el Servidor Flask

Ejecuta el servidor Flask con el siguiente comando:

```bash
python server.py
```

Esto iniciará el servidor Flask en modo de depuración, y podrás ver el mensaje "Hola Mundo Flask!!" en la ruta raíz (http://127.0.0.1:5000/).

## Ver las Bibliotecas Instaladas

Para ver las bibliotecas instaladas en el entorno virtual, usa el comando:

```bash
pip list
```

¡Felicidades! Has configurado tu entorno virtual y creado un proyecto básico en Flask.
