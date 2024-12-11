from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import usuario


class Viaje:
    db_schema = 'viajero_frecuente' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id']
        self.destino = data['destino']
        self.fecha_inicio = data['fecha_inicio']
        self.fecha_fin = data['fecha_fin']
        self.itinerario = data['itinerario']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.organizador_id = data['organizador_id']
        self.unirse = []

    @classmethod
    def borrar_viajes(cls,data):
        query = "delete from viajes where id=%(id)s;"
        return connectToMySQL(cls.db_schema).query_db(query,data)

    @classmethod
    def viajes_con_usuario(cls):
        query = "select * from viajes left join usuarios on usuarios.id=viajes.organizador_id where fecha_inicio > now() order by fecha_inicio asc;"
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        viajes = []
        contador = 0
        for resultado in resultados:
            viajes.append(cls(resultado))
            data_usuario = {
                'id' : resultado['usuarios.id'],
                'nombre' : resultado['nombre'],
                'apellido' : resultado['apellido'],
                'email' : resultado['email'],
                'password' : resultado['password'],
                'updated_at' : resultado['usuarios.updated_at'],
                'created_at' : resultado['usuarios.created_at'],
            }
            viajes[contador].organizador_id = usuario.Usuario(data_usuario)
            viajes[contador].fecha_inicio = str(viajes[contador].fecha_inicio)
            viajes[contador].fecha_fin = str(viajes[contador].fecha_fin)
            contador += 1
        return viajes 
    
    @classmethod
    def viaje_con_unidos(cls,data):
        query = "select * from viajes left join unirse on viajes.id=unirse.viaje_id  left join usuarios on unirse.usuario_id=usuarios.id left join usuarios as usuarios2 on viajes.organizador_id=usuarios2.id where viajes.id=%(id)s;"
        resultados = connectToMySQL(cls.db_schema).query_db(query,data)
        viaje = cls(resultados[0])
        data_organizador = {
            'id' : resultados[0]['usuarios.id'],
            'nombre' : resultados[0]['nombre'],
            'apellido' : resultados[0]['apellido'],
            'email' : resultados[0]['email'],
            'password' : resultados[0]['password'],
            'updated_at' : resultados[0]['usuarios.updated_at'],
            'created_at' : resultados[0]['usuarios.created_at'],
        }
        viaje.organizador_id = usuario.Usuario(data_organizador) 
        for resultado in resultados:
            data_usuario = {
                'id' : resultado['usuarios.id'],
                'nombre' : resultado['nombre'],
                'apellido' : resultado['apellido'],
                'email' : resultado['email'],
                'password' : resultado['password'],
                'updated_at' : resultado['usuarios.updated_at'],
                'created_at' : resultado['usuarios.created_at'],
            }
            viaje.unirse.append(usuario.Usuario(data_usuario))
        return viaje
    
    @classmethod
    def unirse(cls,data):
        query = "insert into unirse (usuario_id,viaje_id) values (%(usuario_id)s,%(viaje_id)s);"
        return connectToMySQL(cls.db_schema).query_db(query,data)

    @classmethod
    def salirse(cls,data):
        query = "delete from unirse where usuario_id=%(usuario_id)s and viaje_id=%(viaje_id)s;"
        return connectToMySQL(cls.db_schema).query_db(query,data)

    @classmethod
    def borrar_unirse(cls,data):
        query = "delete from unirse where viaje_id=%(id)s;"
        return connectToMySQL(cls.db_schema).query_db(query,data)
