from flask import Flask  # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/')          # El decorador "@" asocia la ruta con la función siguiente
def hello_world():
    return 'Hello Francisco Ch'  # Retorna la cadena 'Hello World!' como respuesta

# declaraciones de importacia, tal vez algunas otras rutas
@app.route('/success')
def success():
  return "success"  
# app.run(debug=True) debería ser la ultima declaración! 
@app.route('/hello/<name>') # para una ruta '/hello/____' cualquier cosa despues de '/hello/' se pasa como una variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name
@app.route('/users/<username>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id
if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración