from mysqlconnection import connectToMySQL

class Nave:
    def __init__(self,data):
        self.id = data['id'] 
        self.nombre = data['nombre'] 
        self.modelo = data['modelo'] 
        self.capacidad = data['capacidad'] 
        self.piloto_id = data['piloto_id'] 
        self.created_at = data['created_at'] 
        self.updated_at = data['updated_at'] 

    @classmethod 
    def get_all(cls):
        query = "select * from naves;"
        db_schema = 'starwars_db'
        resultados = connectToMySQL(db_schema).query_db(query)
        naves = []
        for nave in resultados:
            naves.append(cls(nave))
        return naves
    
    @classmethod
    def get_one(cls,data):
        query = "select * from naves where id = %(id)s;"
        db_schema = 'starwars_db'
        result = connectToMySQL(db_schema).query_db(query,data)
        if result:
            return cls(result[0])
        return None

