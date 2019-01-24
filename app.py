from flask import Flask, flash, render_template, url_for, redirect,Response, request, session as flask_session
from database import *
from api import *
import json,requests

app = Flask(__name__)

@app.route('/')
def colored():
    return render_template("index.html")

@app.route('/custom-input/<string:string>')
def corrected(string):
    print(string)
    better_value = correcter(string)
    print(type(better_value))
    print(better_value)
    return render_template("index_corrected.html", displayed= better_value)

@app.route('/grey')
def greyed():
    return render_template("greyed.html")

@app.route('/log-out')
def log_out():
    if 'username' in flask_session:
        del flask_session['username']
        return render_template('index.html')
    else:
        return redirect(url_for('colored'))

@app.route('/log-in', methods=['GET','POST'])
def log_in():
    if request.method == 'POST':
        name = request.form['username']
        password = request.form['psw']
        
        user = query_by_name_and_password(name, password)
        if user is not None and user.password == password:
            flask_session['username'] = user.name
            return render_template('index.html',name=flask_session['username'])
        else :
            error = 'Username & Password do not match , Please try again'
            flash(error)
            return render_template('log_in.html')
    else:       
        return render_template('log_in.html')

@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name = request.form['username'] 
        password = request.form['psw']
        add_User(name,password)
        flash('You were successfully signed up')
        return redirect(url_for('log_in'))
    else:
        return render_template('sign_up.html')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    
    app.debug = True
    app.run()