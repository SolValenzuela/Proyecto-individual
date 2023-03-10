from flask_app import app
from flask import render_template,redirect,request,session,flash, url_for
from flask_app.models.usuario import Usuario
from flask_app.models.horno import Horno
from flask_app.models.agenda import Agenda
from flask_app.controllers import usuarios

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText





@app.route('/about')
def about():
    return render_template('about.html')


#ruta para crear el horno
@app.route('/crear/horno')
def crear_horno():
    if 'usuario_id' not in session:
        flash('Primero tienes que registrarte', 'register')
        return redirect('/login')
    return render_template('horno.html')



# ruta post que procesa y guarda los datos del horno
@app.route('/procesar/horno' , methods=['post'])
def procesar_horno():
    if 'usuario_id' not in session:
        flash('Primero tienes que registrarte', 'register')
        return redirect('/login')
    data={
        'nombre':request.form['nombre'],
        'temperatura_min': request.form['temperatura_min'],
        'temperatura_max': request.form['temperatura_max'],
        "alto" : request.form['alto'],
        'ancho': request.form['ancho'],
        'fondo': request.form['fondo'],
        'costo_bandeja': request.form['costo_bandeja'],
        'costo_medio_horno': request.form['costo_medio_horno'],
        'costo_horno_completo': request.form['costo_horno_completo'],
        'observaciones': request.form['observaciones'],
        'usuario_creador_id':session['usuario_id']
    }
    horno_id=Horno.save(data)
    print (f"horno procesado { horno_id }")
    return redirect(url_for('crear_agenda', horno_id = horno_id))



#ruta para crear las horas de la agenda
@app.route('/crear/agenda/<horno_id>')
def crear_agenda(horno_id):
    if 'usuario_id' not in session:
        flash('Primero tienes que registrarte', 'register')
        return redirect('/login')
    return render_template('crear_agenda.html', horno_id=horno_id)


#ruta para procesar y guardar los datos de la agenda
@app.route('/procesar/agenda/<horno_id>', methods=['POST'])
def procesar_agenda(horno_id):
    if 'usuario_id' not in session:
        flash('Primero tienes que registrarte', 'register')
        return redirect('/login')

    hora_in=request.form['hora_inicio']+':'+request.form['init_min']+':00'
    hora_fin=request.form['hora_termino']+':'+request.form['init_min']+':00'
    print (f"horno procesado en procesar/agenda:  { horno_id }") 
    data={
        'fecha_inicio':request.form['fecha_inicio'],
        'hora_inicio':hora_in,
        'hora_termino':hora_fin,
        'usuario_horno':session['usuario_id'],
        'horno_id':horno_id,
        'agendada':0
    }
    validating=Agenda.validar_agenda(data)
    if not validating:
        flash('Error al crear la fecha','error')
        return redirect('/crear/agenda/<horno_id>')
    else:
        flash('Fecha agregada con ??xito','success')
    Agenda.save(data)
    return redirect('/crear/agenda/<horno_id>')





@app.route('/view/<usuario_id>')
def details(usuario_id):
    if 'taller' not in session:
        flash('Primero tienes que loguearte', 'register')
        return redirect('/login')
    data={
        'usuario_id':usuario_id
    }
    detalle_hornos=Horno.show_horno_details_by_id(usuario_id)
    talleres=Usuario.get_by_id(usuario_id)
    return render_template('show_horno_details.html',detalle_hornos=detalle_hornos,talleres=talleres)




@app.route('/reserva/horno/<horno_id>')
def reserva_horno(horno_id):
    horarios=Agenda.get_by_horno_id(horno_id)
    detalles=Horno.get_all_hornos_with_agenda()
    # reservas=Agenda.reservar_hora(data)
    return render_template('reserva_horno.html', horarios=horarios,detalles=detalles)




# ruta post para procesar y guardar la reserva de hora
@app.route('/procesar/reserva/<id>' , methods=['POST'])
def procesar_reserva(id):

    data={
        'id': id,
        'email':request.form['email'],
        'telefono':request.form['telefono'],
        'agendada':1
    }
    print(f"Revisar paso por procesar reserva { data } ")
    Agenda.reservar_hora(data)

    #agregar env??o de mail 
    print(f"id de agenda para buscar la informaci??n : { id }")
    data = Agenda.get_agenda_by_id(id)
    print(f"datos para email : { data }")

    envio_mail(request.form['email'], data)

    return redirect('/reserva/confirmada')


#ruta para hacer reserva donde se deben ingresar los datos de contacto
@app.route('/detalles/reserva/<id>')
def detalles_reserva(id):
    #detalles_reserva=Agenda.reservar_hora(id)
    return render_template('confirma_reserva.html', id = id)


@app.route('/reserva/confirmada')
def reserva_confirmada():
    return render_template('reserva_confirmada.html')


#??ltima modificaci??n muestra todas las horas disponibles por horno
#listado  hornos del taller que permite agregar horas y eliminar horno
@app.route('/listado/horno')
def horas_by_horno():
    usuario_id = session['usuario_id'] 
    if 'usuario_id' not in session:
        flash('Primero tienes que loguearte', 'register')
        return redirect('/login')
    horarios=Horno.all_hours_by_horno(usuario_id)
    return render_template('horas_by_horno.html', horarios=horarios)




#listado  hornos del taller que permite agregar horas y eliminar horno
@app.route('/actualiza/horno')
def actualiza_horno():
    usuario_id = session['usuario_id'] 
    if 'usuario_id' not in session:
        flash('Primero tienes que loguearte', 'register')
        return redirect('/login')
    horarios=Agenda.get_by_horno_id(usuario_id)
    #detalles_actualizar=Horno.show_horno_details_by_id(usuario_id)
    detalles_actualizar=Horno.show_agenda_horno_by_id(usuario_id)
    return render_template('actualiza_horno.html',detalles_actualizar=detalles_actualizar,horarios=horarios)

    



#arriendo de horno directo desde index,lista todos los hornos
@app.route('/arriendo/horno')
def arriendo_horno():
    hornos_agendas=Horno.get_all_hornos_with_agenda()
    return render_template('hornos_agenda.html',hornos_agendas=hornos_agendas)


#ruta que muestra los hornos ordenados por precio de menor a mayor
@app.route('/precio/menor')
def precio_menor():
    precios=Horno.precio_menor()
    return render_template('precio_menor.html',precios=precios)

    
#ruta para eliminar un horno
@app.route('/destroy/horno/<id>')
def destroy_horno(id):
    if 'taller' not in session:
        flash('Primero tienes que loguearte', 'register')
        return redirect('/login')
    Horno.destroy(id)
    return redirect('/listado/horno/<usuario_id>')



#ruta para eliminar horas
@app.route('/destroy/agenda/<id>')
def destroy_agenda(id):
    if 'usuario_id' not in session:
        flash('Primero tienes que loguearte', 'register')
        return redirect('/login')
    Agenda.destroy(id)
    return redirect('/listado/horno')


@app.route('/prueba/extends')
def extends():
    return render_template('prueba_extends.html')





def envio_mail(mail, datos):
    mail_content = f'''Estimado,

Tienes una reserva en el taller { datos[0].get('nombre_taller')} horno { datos[0].get('nombre_horno')} 

Fecha : { datos[0].get('fecha_inicio') }
Hora inicio : { datos[0].get('hora_inicio') }
Hora termino : { datos[0].get('hora_termino') }
Direccion : { datos[0].get('direccion')}
Comuna : { datos[0].get('comuna')}
'''
    #The mail addresses and password
    sender_address = 'sovalenz@gmail.com'
    sender_pass = 'sjrilesiexefyyec'
    receiver_address = mail
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Tienes una reserva para horno'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')