# Proceso Completo de Despliegue de una Aplicación en Python


## 1. Preparar `requirements.txt`
En tu máquina local, asegúrate de tener el entorno virtual activado y ejecuta el siguiente comando para generar un archivo `requirements.txt` que contenga todas las dependencias del proyecto:

```bash
pip freeze > requirements.txt
```

## 2. Exportar la Base de Datos
Realiza un data export de la base de datos que deseas transferir.
Guarda el script en un archivo .sql.
Abre el archivo .sql en un editor de texto como Notepad o MySQL Workbench para verificar el contenido.

## 3. Subir el Repositorio a GitHub
Crea un repositorio en GitHub.
En tu proyecto local, inicializa el repositorio:


## 4. Crear una Instancia EC2 en AWS
Inicia sesión en AWS.
Busca EC2 en la consola y selecciona "Lanzar Instancia".
Asigna un nombre a tu instancia.
Selecciona la imagen Ubuntu Server 22.04.
Elige el tipo de instancia t2.micro.
Crea un par de claves para conectarte al servidor.
Descarga y guarda el archivo .pem en el mismo repositorio donde esta nuestro proyecto.
Configura la seguridad:
- Limita el acceso SSH a tu IP.
- Habilita el tráfico HTTP y HTTPS.
Haz clic en "Lanzar Instancia".

## 5. Conectarse al Servidor EC2

Conéctate al servidor mediante SSH con tu Gitbash, pero asegurate que estas ubicado en el folder donde este la llave:

```bash
ssh -i "tu_clave.pem" ubuntu@<tu_ip_publica>
```

## 6. Instalar Librerías Básicas en el Servidor
Ejecuta los siguientes comandos para actualizar el servidor e instalar las dependencias necesarias:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-pip nginx git -y
sudo apt-get install python3-venv
sudo apt-get install mysql-server
sudo apt-get update
```

## 7. Configurar MySQL
Accede al servidor MySQL:

```bash
sudo mysql -u root -p
```

Configura el usuario root:

```sql
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root';
FLUSH PRIVILEGES;
quit;
```

Asegura la instalación:

```bash
sudo mysql_secure_installation
```

- Validar contraseña: n
- Cambiar contraseña root: n
- Eliminar usuarios anónimos: y
- Prohibir acceso remoto de root: y
- Eliminar la base de datos de prueba: y

## 8. Importar la Base de Datos en el Servidor
Conéctate a MySQL:

```bash
mysql -u root -p
```

Copia y pega el contenido del archivo .sql para importar la base de datos.
Verifica que se haya cargado correctamente:

```sql
SHOW DATABASES;
```

Sal de MySQL:

```bash
exit;
```

## 9. Clonar el Repositorio en el Servidor
Clona el repositorio en tu servidor EC2:
Ejemplo:

```bash
git clone https://github.com/kjacome24/heroes.git
```

## 10. Configurar el Ambiente Virtual
Crea y activa el ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instala las dependencias del archivo requirements.txt:

```bash
pip3 install -r requirements.txt
pip3 install gunicorn
```

## 11. Crear el Archivo WSGI
Crea un archivo llamado wsgi.py:

```bash
sudo nano wsgi.py
```

Contenido del archivo:

```python
from server import app as application
if __name__ == "__main__":
    application.run()
```

## 12. Probar Gunicorn
Ejecuta Gunicorn para probar si hay errores:

```bash
gunicorn --bind 0.0.0.0:5000 wsgi:application
```

Si todo funciona bien, presiona Ctrl + C para detener el servidor.

Tambien desactiva el ambiente virtual:

```bash
deactivate
```


## 13. Configurar Gunicorn como un Servicio
Crea un archivo de servicio para Gunicorn:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Contenido del archivo(Cambia el nombre heroes por el nombre de tu proyecto):

```makefile
[Unit]
Description=Gunicorn instance
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/heroes
Environment="PATH=/home/ubuntu/heroes/venv/bin"
ExecStart=/home/ubuntu/heroes/venv/bin/gunicorn --workers 3 --bind unix:heroes.sock -m 007 wsgi:application

[Install]
WantedBy=multi-user.target
```

Inicia y habilita el servicio:

```bash
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

## 14. Configurar Nginx
Crea un archivo de configuración para Nginx (Cambia heroes por el nombre del proyecto):

```bash
sudo nano /etc/nginx/sites-available/heroes
```

Contenido del archivo (cambia TU_IP_PUBLICA por la ip de tu instancia):

```perl
server {
    listen 80;
    server_name TU_IP_PUBLICA;

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/ubuntu/heroes/heroes.sock;
    }
}
```

## 15. Configurar Nginx
Activa el sitio (Cambia heroes por el nombre de tu proyecto):

```bash
sudo ln -s /etc/nginx/sites-available/heroes /etc/nginx/sites-enabled
sudo nginx -t
sudo rm /etc/nginx/sites-enabled/default
sudo service nginx restart
```

Ajusta los permisos:

```bash
sudo chmod 755 /home/ubuntu
```

## Finalizar y Acceso desde el Navegador
Accede a la IP pública de tu instancia desde un navegador para confirmar que el despliegue fue exitoso.

¡Listo!