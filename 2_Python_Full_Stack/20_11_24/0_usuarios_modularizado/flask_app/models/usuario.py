from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
    db_schema = 'usuarios_practica'
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "select * from usuarios;"
        
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))
        return usuarios
    
    @classmethod
    def get_one(cls,data):
        query = "select * from usuarios where id=%(id)s;"
        result = connectToMySQL(cls.db_schema).query_db(query,data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def eliminar(cls,data):
        query = "delete from usuarios where id=%(id)s;"
        return connectToMySQL(cls.db_schema).query_db(query,data)

    @classmethod
    def crear(cls,data):
        query = "insert into usuarios (nombre,apellido,email) values (%(nombre)s,%(apellido)s,%(email)s);"
        return connectToMySQL(cls.db_schema).query_db(query,data)
    
    @classmethod
    def actualizar(cls,data):
        query = "update usuarios set nombre = %(nombre)s, apellido=%(apellido)s,email=%(email)s where id=%(id)s;"
        return connectToMySQL(cls.db_schema).query_db(query,data)
