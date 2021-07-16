from flask import Flask, render_template, request, redirect
from mysqlconnection import connectToMySQL

app = Flask(__name__)
@app.route("/users")
def index():
    mysql = connectToMySQL('people')
    people = mysql.query_db('SELECT * FROM user;')
    return render_template ("users.html", all_users = people)

@app.route("/users/new")
def getCreateUser():
    return render_template('create.html')


@app.route("/users/create", methods=["POST"])
def createUser():
    mysql=connectToMySQL("people")

    query = "INSERT INTO user (fname, lname, email, created_at, updated_at) VALUES (%(fname)s, %(lname)s, %(email)s, NOW(), NOW());"
    data ={
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email']
    }

    user=mysql.query_db(query, data)
    return redirect(f'/users/{user}')

@app.route("/users/<id>")
def showUser(id):
    mysql=connectToMySQL("people")
    query ="SELECT * FROM user WHERE id=%(id)s;"
    data ={
        "id": id
    }
    user=mysql.query_db(query, data)
    user=user[0]
    return render_template('show.html', user=user)


@app.route("/users/<id>/edit")
def editUser(id):
    mysql=connectToMySQL("people")

    query ="SELECT * FROM user WHERE id=%(id)s;"
    data ={
        "id": id
    }
    user=mysql.query_db(query, data)
    user=user[0]
    return render_template('edit.html', user=user)

@app.route("/users/<id>/update", methods=['POST'])
def updateUsers(id):
    mysql=connectToMySQL("people")
    query ="UPDATE user SET fname=%(fname)s, lname=%(lname)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
    data ={
        "fname": request.form['fname'],
        "lname": request.form['lname'],
        "email": request.form['email'],
        "id": id
    }
    mysql.query_db(query, data)
    return redirect (f'/users/{id}')

@app.route("/users/<id>/destroy")
def destroyusers(id):
    mysql=connectToMySQL("people")
    query ="DELETE FROM user WHERE id=%(id)s;"
    data ={
        "id": id
    }
    mysql.query_db(query, data)
    return redirect ('/users')

if __name__ == "__main__":
    app.run(debug=True)