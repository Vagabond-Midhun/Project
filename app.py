from flask import Flask, render_template,url_for,request
from database import get_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Signin')
def Signin():
    return render_template('Signin.html')

@app.route('/Reg')
def Reg():
    return render_template('Reg.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/marriage')
def marriage():
    return render_template('marriage.html')

@app.route('/password')
def password():
    return render_template('password.html')

if __name__ == '__main__':
    app.run()