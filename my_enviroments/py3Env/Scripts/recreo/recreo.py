from flask import Flask, render_template, session, redirect, url_for  # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/play/<x>/<id>') # para una ruta '/users/____/____', dos parámetros en la url se pasan como nombre de usuario e id
def show_user_profile(x,color):
    try:
        print(x)
        print(color)
        x=int(x)
    except:
        return 'Lo siento! Sin respuesta. Inténtelo de nuevo!'
    return render_template('recre.html', col= color , rep = range(x)) 
if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración