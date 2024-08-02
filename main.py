from flask import Flask, render_template,url_for,request,redirect,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors,re,hashlib



app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'project'

mysql = MySQL(app)


@app.route('/project/', methods=['GET', 'POST'])
def login():
    
    
    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        
        
        username = request.form['username']
        password = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM admin WHERE username = %s AND password = %s', (username, password,))
       
        admin = cursor.fetchone()
        
        if admin:
           
            session['loggedin'] = True
            session['id'] = admin['id']
            session['username'] = admin['username']

            
   
        else: request.method == 'POST' and 'username' in request.form and 'password' in request.form
        
        
        username = request.form['username']
        password = request.form['password']
       
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pythonlogin WHERE username = %s AND password = %s', (username, password,))
       
        pythonlogin = cursor.fetchone()
        
        if pythonlogin:
           
            session['loggedin'] = True
            session['id'] = pythonlogin['id']
            session['username'] = pythonlogin['username']

            
           
        else:
            
            msg = 'Incorrect username/password!'
    
    return render_template('main.html')

@app.route('/project/logout')
def logout():
    
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   
   return redirect(url_for('index'))

@app.route('/project/register', methods=['GET', 'POST'])
def register():
   
    msg = ''
    
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pythonlogin WHERE username = %s', (username,))
        pythonlogin = cursor.fetchone()
        
        if pythonlogin:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
           
            
            
            cursor.execute('INSERT INTO pythonlogin VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'

            
    elif request.method == 'POST':
       
        msg = 'Please fill out the form!'
    
    return render_template('Signin.html', msg=msg)

@app.route('/project/home')
def home():
    
    if 'loggedin' in session:
       
        return render_template('main.html', username=session['username'])
    
    return redirect(url_for('login'))

@app.route('/project/profile')
def profile():
    
    if 'loggedin' in session:
        
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM pythonlogin WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        
        return render_template('profile.html', account=account)
    
    return redirect(url_for('login'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Signin')
def Signin():
    return render_template('Signin.html')

@app.route('/Reg')
def Reg():
    return render_template('Reg.html')



@app.route('/project/main')
def main():
    return render_template('main.html')

@app.route('/project/base')
def base():
    return render_template('base.html')



@app.route('/project/marriage')
def marriage():
    return render_template('marriage.html')



@app.route('/project/HIMTEE')
def HIMTEE():
    return render_template('HIMTEE.html')

@app.route('/project/content3')
def content3():
    return render_template('content3.html')

@app.route('/project/content4')
def content4():
    return render_template('content4.html')

@app.route('/project/content5')
def content5():
    return render_template('content5.html')

@app.route('/project/content6')
def content6():
    return render_template('content6.html')

@app.route('/project/content7')
def content7():
    return render_template('content7.html')

@app.route('/project/content8')
def content8():
    return render_template('content8.html')

@app.route('/project/content9')
def content9():
    return render_template('content9.html')

@app.route('/project/content10')
def content10():
    return render_template('content10.html')


if __name__ == '__main__':
    app.run()