from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from datetime import datetime


db_name='nueva_prueba_proyecto'

class Agenda:
    
    def __init__(self,data):
        self.id = data['id']
        self.fecha_inicio= data['fecha_inicio']
        self.hora_inicio=data['hora_inicio']
        self.hora_termino=data['hora_termino']
        self.usuario_horno= data['usuario_horno']
        self.agendada= data['agendada']
        self.email= data['email']
        self.telefono= data['telefono']
        self.horno_id=data['horno_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#guardar los datos de la agenda
    @classmethod
    def save(cls,data):
        query = "INSERT INTO agendas (fecha_inicio,hora_inicio,hora_termino,usuario_horno,horno_id,agendada) VALUES (%(fecha_inicio)s,%(hora_inicio)s,%(hora_termino)s,%(usuario_horno)s,%(horno_id)s,%(agendada)s);"
        results= connectToMySQL(db_name).query_db(query,data)
        return results
    

#obtener todos los datos de la agenda
    @classmethod
    def get_agenda_by_id(cls, id):
        query = '''SELECT fecha_inicio, hora_inicio, hora_termino, h.nombre nombre_horno, u.nombre nombre_taller, u.direccion, u.comuna 
                    FROM agendas a
                    INNER JOIN hornos h
                    ON a.horno_id = h.id
                    INNER JOIN usuarios u
                    ON u.id = a.usuario_horno
                    WHERE a.id = %(id)s;'''
        data = { 'id' : id}
        agendas =  connectToMySQL(db_name).query_db(query, data)

        return agendas


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM agendas;"
        agendas =  connectToMySQL(db_name).query_db(query)

        agenda =[]
        for b in agendas:
            agenda.append(cls(b))
        return agenda

#selecciona los horarios disponibles por el usuario creador
    @classmethod
    def get_by_id_user_creator(cls,usuario_horno):
        data={
            'usuario_horno':usuario_horno
        }
        query = """
                /*selecciona horario por usuario creador*/
                SELECT * FROM agendas 
                WHERE usuario_horno=%(usuario_horno)s;"""

        result =  connectToMySQL(db_name).query_db(query,data)
        return result


#selecciona los horarios disponibles del horno
    @classmethod
    def get_by_horno_id(cls,horno_id):
        data={
            'horno_id':horno_id
        }
        query = """
                /*selecciona horario por id de horno*/
                SELECT * FROM agendas 
                WHERE horno_id=%(horno_id)s AND agendada = 0;"""

        result =  connectToMySQL(db_name).query_db(query,data)
        return result


#actualizar estado de reserva
    @classmethod
    def reservar_hora(cls,data):
        query= """
                /* query para agendar las horas*/
                UPDATE agendas
                set agendada = %(agendada)s ,    /* marca para agendar */
                    email = %(email)s,
                    telefono = %(telefono)s
                WHERE id = %(id)s; /* id de la agenda*/
                """
        result=connectToMySQL(db_name).query_db(query,data)
        return result



#elimina una hora
    @classmethod
    def destroy(cls,data):
        data={'id':data}
        query= "DELETE from agendas WHERE id=%(id)s;"
        results=connectToMySQL(db_name).query_db(query,data)
        return results   





#validar fechas disponibles
    @staticmethod
    def validar_agenda(fecha):
        is_valid = True
        fecha_inicio=fecha['fecha_inicio'].strip()
        if fecha_inicio == '':
            flash('fecha de inicio no puede estar vacía','error')
            is_valid= False
        if len(fecha['fecha_inicio']) <1:
            flash('fecha de inicio no puede estar vacía','error')
            is_valid=False
        hora_inicio= fecha['hora_inicio'].strip()
        if hora_inicio == '':
            flash('hora de inicio no puede estar vacía','error')
            is_valid= False
        if len(fecha['hora_inicio']) <2:
            flash('Hora de inicio no puede estar vacía','error')
            is_valid= False
        hora_termino= fecha['hora_termino'].strip()
        if hora_termino == '':
            flash('Hora de termino no puede estar vacía','error')
            is_valid= False
        if len(fecha['hora_termino']) <2:
            flash('Hora de termino no puede estar vacía','error')
            is_valid= False
        fecha_inicio=fecha['fecha_inicio'] 
        if fecha_inicio < datetime.now().strftime("%Y-%m-%d"):
            flash('Fecha debe ser igual o mayor a la actual','error')
            is_valid=False
            
        return is_valid


