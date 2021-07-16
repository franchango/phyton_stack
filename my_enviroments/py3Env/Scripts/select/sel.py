__author__ = 'fchango'
from flask import Flask, request, g, redirect, url_for, abort, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def usuarios():

    #resultado de SELECT id, nombre FROM usuarios ORDER BY nombre
    res = [{'id': 1, 'nombre': 'Fulano'}, {'id': 2, 'nombre': 'Fulanito'}]
    usuarios = [(di['id'], di['nombre']) for di in res]
    return render_template('usuarios.html', usuarios=usuarios)
if __name__ == '__main__':
    app.run(debug=True)