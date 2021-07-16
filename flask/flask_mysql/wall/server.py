from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import time
import re
import md5

app = Flask(__name__)
app.secret_key = "waow"
mysql = MySQLConnector(app,'walldb')

@app.route('/')
def index():
    session["loggedOn"] = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
    #sign in logic
    if request.form['action'] == 'signIn':
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        check = "SELECT * FROM users"
        for i in (mysql.query_db(check)):
            if i['email'] == email and i['password'] == hashed_password:
                session['email'] = email
                session['loggedOn'] = True
                q1 = "SELECT first_name FROM users where email = '{}'".format(session['email'])
                l1 = mysql.query_db(q1)
                session['name'] = l1[0]['first_name']
                print session['name']
                flash("Welcome {} {}!".format(i['first_name'], i['last_name']))
                return redirect('/success')
        flash('incorrect email/password combo')
        return redirect('/')

    #register logic
    else:
        #get data from forms
        first = request.form['firstName']
        last = request.form['lastName']
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        confirm = request.form['confirm']
        

        data = { #change password to hashed_password below
                'first_name': first,
                'last_name': last,
                'email': email,
                'password': hashed_password
                }
        #set all data in a dictionary
        
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
        
        properLogin = True
        if len(first) < 3:
            flash("first name must be at least 2 letters long")
            properLogin = False

        if len(last) < 3:
            flash("last name must be at least 2 letters long")
            properLogin = False

        my_re = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        check = "SELECT * FROM users"
        for i in (mysql.query_db(check)):
            if i['email'] == email:
                flash("email already in database")
                properLogin = False
        if not my_re.match(email):
            flash("please use a proper email")
            properLogin = False
        
        if len(password) < 8:
            flash("password must be at least 8 characters long")
            properLogin = False
        if password != confirm:
            flash("passwords must match")
            properLogin = False
        
        if properLogin:
            mysql.query_db(query, data)
            flash("Welcome to this pointless website {} {}!".format(first, last))
            session['loggedOn'] = True
            session['email'] = email
            return redirect('/success')
        else:
            return redirect('/')


@app.route('/success')
def success():
    print session['email']
    if session['loggedOn'] == False:
        flash("you must be signed in to see this content")
        return redirect('/')

    query = "SELECT users.first_name, messages.message, messages.id FROM users JOIN messages ON users.id = messages.users_id ORDER BY messages.id DESC"
    messages = mysql.query_db(query)
    query2 = "SELECT users.first_name, messages.id, comments.comment FROM comments JOIN messages ON messages.id = comments.messages_id JOIN users ON users.id = comments.users_id"

    comments = mysql.query_db(query2)
    return render_template("success.html", messages = messages, comments = comments)

@app.route('/process2', methods=['POST'])
def update():
    #q1 for querry1 and d1 for returned dictionary
    q1 = "SELECT id FROM users where email = '{}'".format(session['email'])
    d1 = mysql.query_db(q1)
    current_id = d1[0]['id']
    
    if request.form['action'] == 'message':
        message = request.form['message']
        data = {'message': message, 'id' : current_id}
        query = "INSERT INTO messages (message, created_at, users_id) VALUES (:message, NOW(), :id)"
        messages = mysql.query_db(query, data)

    else: #add message id somehow
        mID = request.form['action']
        print mID
        comment = request.form['comment']
        data = {'comment': comment, 'id' : current_id, 'messages_id': mID}
        query = "INSERT INTO comments (comment, created_at, users_id, messages_id) VALUES (:comment, NOW(), :id, :messages_id)"
        comments = mysql.query_db(query, data)
    return redirect('/success')

    


app.run(debug=True)
