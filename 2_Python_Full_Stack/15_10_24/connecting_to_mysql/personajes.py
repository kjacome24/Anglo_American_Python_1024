from mysqlconnection import connectToMySQL

class Personaje:
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.año_nacimiento = data['año_nacimiento']
        self.planeta_id = data['planeta_id']
        self.especie_id = data['especie_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "select * from personajes;"
        resultados = connectToMySQL('starwars_db').query_db(query)
        personajes = []
        for personaje in resultados:
            personajes.append(cls(personaje))
        return personajes