import requests
#ort an dem wir alle api funktionen hinschreiben
#wenn man innerhalb einer methode eine variable vergibt, ist diese ausserhalb der methode nicht verwendbar

def getToken(user, password):
   credentials = {'username':user, 'password':password}
   r = requests.post('https://api.europace.de/login', data=credentials)
   print (r)
   if r.status_code/100==2:
       token=r.json()['access_token']
       loginSuccessful = True
   else:
       token=""
       loginSuccessful = False
   return token, loginSuccessful

def getVorgang(vorgangsnummer):
    url = 'https://api.europace2.de/v2/vorgaenge/' + vorgangsnummer
    r = request.get(url, headers=headers)
    return r.content
