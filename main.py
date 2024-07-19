from flask import Flask, render_template,url_for,request,redirect,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors,re,hashlib

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'pythonlogin'

mysql = MySQL(app)

@app.route('/pythonlogin/', methods=['GET', 'POST'])
def login():
    
    msg = ''
   
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        username = request.form['username']
        password = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
       
        account = cursor.fetchone()
        
        if account:
           
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
           
            return 'Logged in successfully!'
        else:
            
            msg = 'Incorrect username/password!'
    
    return render_template('main.html', msg=msg)

@app.route('/pythonlogin/logout')
def logout():
    
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   
   return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signin')
def Signin():
    return render_template('Signin.html')

@app.route('/Reg')
def Reg():
    return render_template('Reg.html')

@app.route('/password')
def password():
    return render_template('password.html')

@app.route('/pythonlogin/main')
def main():
    return render_template('main.html')

@app.route('/pythonlogin/base')
def base():
    return render_template('base.html')

@app.route('/pythonlogin/profile')
def profile():
    return render_template('profile.html')

@app.route('/pythonlogin/marriage')
def marriage():
    return render_template('marriage.html')

if __name__ == '__main__':
    app.run()