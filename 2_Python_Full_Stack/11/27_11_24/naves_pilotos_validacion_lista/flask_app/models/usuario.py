from flask_app.config.mysqlconnection import connectToMySQL ###Nos podemos conectar a la BD y podemos jugar con la creacion del objeto y sus metodos

#####aqui debes importar otras clases en caso de que sea necesario
from flask import flash

class Usuario:
    db_schema = 'piloto_naves' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id'] 
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.friends = []

    @classmethod
    def get_all(cls):
        query = "select * from pilotos;" ###cambiar la tabla a la que apuntamos.
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        usuarios = [] ###Cambiar el nombre del arreglo para algo que represente la tabla
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios


    
    @classmethod
    def save(cls,data):
        query = "insert into pilotos (first_name,last_name,email) values (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(cls.db_schema).query_db(query,data)
    ####Aca hacemos la validacion
    @staticmethod
    def validar_usuario(data):
        is_valid = True
        if len(data['first_name']) < 3:
            flash(["El primer nombre es muy corto, debe tener 3 letras por lo menos!",0])
            is_valid = False
        if len(data['last_name']) < 3:
            flash(["El primer apellido es muy corto, debe tener 3 letras por lo menos!",0])
            is_valid = False
        return is_valid

    