from flask import Flask, render_template, session, redirect, url_for  # Importar Flask para que permita crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"
@app.route('/lists')
def render_lists():
    # Muy pronto, obtendremos datos de una base de datos, pero por ahora, estamos codificando datos
    student_info = [
       {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("lists.html", random_numbers = [3,1,5], students = student_info)
if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración