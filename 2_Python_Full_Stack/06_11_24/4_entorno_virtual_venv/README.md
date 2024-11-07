# Configuración de Entorno Virtual con venv

Este documento proporciona instrucciones paso a paso para configurar un entorno virtual con venv e instalar Flask.

## Crear un Entorno Virtual

Ejecuta el siguiente comando en la terminal para crear un entorno virtual llamado `entorno_virtual`:

```bash
python -m venv entorno_virtual
```

## Activar el Entorno Virtual

Activa el entorno virtual usando el comando correspondiente según el tipo de terminal en tu sistema operativo:

### Command Prompt:
```cmd
entorno_virtual\Scripts\activate
```
### PowerShell:
```powershell
.\entorno_virtual\Scripts\Activate
```

Una vez que el entorno virtual esté activado, verás `(entorno_virtual)` al inicio de la línea en la terminal, indicando que estás en el entorno virtual.


## Instalar Flask

Con el entorno virtual activo, instala Flask usando el siguiente comando:

```bash
pip install flask
```

## Ver las Bibliotecas Instaladas

Para ver las bibliotecas instaladas en el entorno virtual, usa el comando:

```bash
pip list
```

## Desactivar el Entorno Virtual

Cuando termines de usar el entorno virtual, puedes desactivarlo con el siguiente comando:

```bash
deactivate
``

¡Felicidades! Has configurado tu entorno virtual e instalado Flask.
