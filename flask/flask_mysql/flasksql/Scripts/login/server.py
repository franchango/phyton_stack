from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import time
import re
from hashlib import md5

app = Flask(__name__)
app.secret_key = "waow"
mysql = MySQLConnector(app,'lnrdb')

@app.route('/')
def index():
    session["loggedOn"] = False
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def create():
    if request.form['action'] == 'signIn':
        email = request.form['email']
        password = request.form['password']
        hashed_password = md5.new(password).hexdigest()
        check = "SELECT * FROM users"
        for i in (mysql.query_db(check)):
            #change password to hashed_password below
            if i['email'] == email and i['password'] == hashed_password:
                session['loggedOn'] = True
                flash("Welcome {} {}!".format(i['first_name'], i['last_name']))
                return redirect('/success')
        flash('incorrect email/password combo')
        return redirect('/')

        '''
        1) make a query call to see if both the username are in the db and that they
        belong to the same user
        2) if not, redirect to index and set a flash message for incorrect login
        '''
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
            return redirect('/success')
        else:
            return redirect('/')

        
    

@app.route('/success')
def success():

    return render_template("success.html")

    

app.run(debug=True)
