from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.usuario import Usuario
from flask_app.models.horno import Horno


from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app) 

@app.route('/')
def home():
    talleres=Horno.get_taller_agenda()
    return render_template('index.html',talleres=talleres)


@app.route('/registro')
def registro_usuario():
    return render_template('registro.html')



#ruta Post de formulario de registro de usuario,guarda los datos del nuevo usuario y redirige
@app.route('/procesar/usuario', methods=['POST'])
def procesar_usuario():
    is_valid= Usuario.validar_usuario(request.form)
    print(is_valid)
    if not is_valid:
        print('No valido')
        return redirect('/registro')
    
    nuevo_usuario = {
        "nombre":request.form['nombre'],
        "direccion":request.form['direccion'],
        "comuna":request.form['comuna'],
        "email": request.form['email'],
        "password":bcrypt.generate_password_hash(request.form['password']),    
    }
    id = Usuario.save(nuevo_usuario)
    if not id:
        flash("The email already exists.","register")
        return redirect('/login')
    session['username'] = request.form['nombre']
    session['usuario_id'] = id
    return redirect('/crear/horno')


#ruta para loguearse
@app.route('/login')
def login():
    return render_template('login.html')


# ruta Post de formulario login,comprueba que usuario existe,guarda datos de session y redirige
@app.route("/procesar/login",methods=['POST'])
def procesar_login():


    data = {
        "email": request.form['email']
    }
    usuario = Usuario.get_by_email(data)
    if not usuario:
        flash("Email or password invalido","register")
        print('Email or password invalido","register')
        return redirect("/login")
    
    if not bcrypt.check_password_hash(usuario.password,request.form['password']):
        flash("Email or password invalido","register")
        return redirect("/login")
    session['usuario_id'] =usuario.id
    session['taller']=usuario.nombre
    
    return redirect('/listado/horno')



@app.route('/proximamente')
def proximamente():
    return render_template('proximamente.html')


#Ruta para desloguearse
@app.route('/logout')
def close_session():
    session.clear()
    return redirect('/')




