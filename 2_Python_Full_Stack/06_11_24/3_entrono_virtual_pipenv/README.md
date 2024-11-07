# Configuración de Entorno Virtual e Instalación de Flask con Pipenv

## Configuración Inicial del Directorio
1. **Navega al directorio de tu proyecto y crea una nueva carpeta para el entorno:**
    ```bash
    mkdir 3_entorno_pipenv
    cd 3_entorno_pipenv
    ```

## Instalación de Pipenv
2. **Instala Pipenv si aún no está instalado:**
    ```bash
    pip install pipenv
    ```
    - Este comando instala Pipenv, que gestiona los entornos virtuales y las dependencias del proyecto.

## Creación y Activación del Entorno Virtual
3. **Inicializa y activa el entorno virtual utilizando Pipenv:**
    ```bash
    pipenv shell
    ```
    - Este comando crea un entorno virtual específico para tu proyecto y lo activa.

## Instalación de Flask
4. **Instala Flask dentro del entorno virtual activado:**
    ```bash
    pip install flask
    ```
    - Instala Flask dentro del entorno virtual para asegurar que todas las dependencias del proyecto estén contenidas.

## Verificación de la Instalación y Activación del Entorno
5. **Lista los paquetes instalados para verificar la instalación de Flask:**
    ```bash
    pip list
    ```
    - Muestra una lista de todos los paquetes instalados dentro del entorno virtual, incluyendo Flask y sus dependencias.

6. **Representación visual del entorno virtual activado:**
    - Muestra cómo cambia la terminal cuando el entorno virtual está activado, típicamente mostrando el nombre del entorno en el prompt de comandos.

## Salir del Entorno Virtual
7. **Desactiva el entorno virtual cuando hayas terminado:**
    ```bash
    exit
    ```
    - Sale del entorno virtual y retorna a los ajustes predeterminados del sistema.

Siguiendo estos pasos, habrás configurado un entorno virtual utilizando Pipenv, instalado Flask y asegurado que tu proyecto esté listo para el desarrollo. Esta configuración proporciona un ambiente de desarrollo controlado y consistente para proyectos en Python.

