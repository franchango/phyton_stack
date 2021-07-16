from flask import Flask, render_template, session, redirect, url_for  # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
def hello_world():
    return '¡Hola mundo!'  # Retorna la cadena 'Hello World!' como respuesta
# declaraciones de importacia, tal vez algunas otras rutas
@app.route('/dojo')
def success():
  return 'Dojo!'  
# app.run(debug=True) debería ser la ultima declaración! 
@app.route('/say/flask') # para una ruta '/hello/____' cualquier cosa despues de '/hello/' se pasa como una variable 'name'
def say():
    return '¡Hola frask!'
@app.route('/say/michael') # para una ruta '/hello/____' cualquier cosa despues de '/hello/' se pasa como una variable 'name'
def name():
    return '¡Hola Michael!'
@app.route('/say/john') # para una ruta '/hello/____' cualquier cosa despues de '/hello/' se pasa como una variable 'name'
def named():
    return '¡Hola John!'
@app.route('/say/<name>') # para una ruta '/hello/____' cualquier cosa despues de '/hello/' se pasa como una variable 'name'
def hola(name):
    print(name)
    return "hola " + name
@app.route('/repeat/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username,id):
    try:
        print(username)
        print(id)
        id=int(id)
    except:
        return 'Lo siento! Sin respuesta. Inténtelo de nuevo!'
    return render_template('index.html', my_string= username , mylist = range(id)) 
if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración