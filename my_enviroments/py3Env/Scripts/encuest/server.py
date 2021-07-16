from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # asignar una clave secreta por motivos de seguridad
# nuestra ruta de indice se encargara de representar nuestro formulario
@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template("index.html")    
@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    email_from_form = request.form['email']
    return render_template("show.html", name_on_template=request.form['name'], email_on_template=request.form['email'])
@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template('show.html')

if __name__=="__main__":   # Asegúrese de que este archivo se ejecute directamente y no desde un módulo diferente
    app.run(debug=True)    # ejecuta la aplicación en modo depuración