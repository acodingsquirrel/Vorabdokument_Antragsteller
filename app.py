from flask import Flask, render_template, request, session
from random import randrange
import api_client

app = Flask(__name__)
app.config['SECRET_KEY']='\x8d\x14\xd2 a\xb3Zl\xf2\xe2\xc1\xac\r\xc6\xe2\x15\xc3\xeb3\x99\xe7NiR'

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/bestaetigt', methods=['get', 'post'] )
def bestaetigt():
    user=request.form['partnerid']
    passwort=request.form['passwort']
    token, loginSuccessful = api_client.getToken(user, passwort)
    if loginSuccessful:
        session['token']= token
        return render_template('bestaetigt.html',token=token)
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
