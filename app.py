from flask import Flask, render_template, request, session, redirect
from random import randrange
import api_client

app = Flask(__name__)
app.config['SECRET_KEY']='\x8d\x14\xd2 a\xb3Zl\xf2\xe2\xc1\xac\r\xc6\xe2\x15\xc3\xeb3\x99\xe7NiR'

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/pruefelogin', methods=['get', 'post'] )
def pruefelogin():
    user=request.form['partnerid']
    passwort=request.form['passwort']
    token, loginSuccessful = api_client.getToken(user, passwort)
    if loginSuccessful:
        session['token']= token
        return redirect('/bestaetigt')
    else:
        return render_template('login.html')

@app.route('/bestaetigt')
def bestaetigt():
   return render_template('bex.html', token=session.get('token'))

if __name__ == '__main__':
    app.run(debug=True)
