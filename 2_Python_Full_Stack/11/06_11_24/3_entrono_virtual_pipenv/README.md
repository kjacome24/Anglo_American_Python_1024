# Configuración de Entorno Virtual e Instalación de Flask con Pipenv

## Configuración Inicial del Directorio
1. **Navega al directorio de tu proyecto y crea una nueva carpeta para el entorno:**
    ```bash
    mkdir example
    cd example
    ```

## Instalación de Pipenv
2. **Instala Pipenv si aún no está instalado:**
    ```bash
    pip install pipenv
    ```
    - Este comando instala Pipenv, que gestiona los entornos virtuales y las dependencias del proyecto. Asegúrate de que está correctamente instalado y observa cualquier mensaje sobre actualizaciones necesarias.

## Creación y Activación del Entorno Virtual
3. **Inicializa y activa el entorno virtual utilizando Pipenv:**
    ```bash
    pipenv install flask
    ```
    - Este comando no solo instala Flask sino que también crea un entorno virtual para el proyecto si no existe uno previamente, como indicado por la creación del `Pipfile` y `Pipfile.lock`.

## Verificación de la Instalación y Activación del Entorno
4. **Activa el entorno virtual y verifica la instalación:**
    ```bash
    pipenv shell
    pip list
    ```
    - Al activar el entorno con `pipenv shell`, te mueves a un subshell donde el entorno virtual está activo. El comando `pip list` mostrará Flask y sus dependencias que fueron instaladas.

## Salir del Entorno Virtual
5. **Desactiva el entorno virtual cuando hayas terminado:**
    ```bash
    exit
    ```
    - Este comando te saca del entorno virtual y vuelve a la configuración normal de tu sistema.

## Revisión Final del Directorio
6. **Verifica los archivos en el directorio para confirmar la creación de `Pipfile` y `Pipfile.lock`:**
    ```bash
    dir
    ```
    - Este paso confirma la presencia de `Pipfile` y `Pipfile.lock` en tu directorio, indicando que las dependencias están siendo gestionadas correctamente.

Siguiendo estos pasos, habrás configurado un entorno virtual utilizando Pipenv, instalado Flask y asegurado que tu proyecto esté listo para el desarrollo. Esta configuración proporciona un ambiente de desarrollo controlado y consistente para proyectos en Python.
