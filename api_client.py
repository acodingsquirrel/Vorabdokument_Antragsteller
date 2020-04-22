# -*- coding: utf-8 -*-
import requests
import xmltodict

#ort an dem wir alle api funktionen hinschreiben
#wenn man innerhalb einer methode eine variable vergibt, ist diese ausserhalb der methode nicht verwendbar

def getPruefen(user, password):
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

url = 'https://www.europace2.de/baufiSmart/soap/bex/v13/vorgangAnlegen' #PROD

def makeBody(partner_id, api_key):
    myBody =  '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:bex="www.europace2.de/baufiSmart/bex/schema/bex-v13-VorgangAnlegen">'
    myBody += '     <soapenv:Header>'
    myBody += '         <bex:LoggingId>'+partner_id+'</bex:LoggingId>'
    myBody += '         <bex:DatenKontext>ECHTGESCHAEFT</bex:DatenKontext>'
    myBody += '         <bex:EmpfaengerPartnerId>'+partner_id+'</bex:EmpfaengerPartnerId>'
    myBody += '         <bex:BearbeiterPartnerId>'+partner_id+'</bex:BearbeiterPartnerId>'
    myBody += '         <bex:ApiKey>'+api_key+'</bex:ApiKey>'
    myBody += '     </soapenv:Header>'
    myBody += '     <soapenv:Body>'
    myBody += '         <bex:Vorgang xmlns:bex="www.europace2.de/baufiSmart/bex/schema/bex-v13-VorgangAnlegen">'
    myBody += '             <erfassteDaten>'
    myBody += '             </erfassteDaten>'
    myBody += '         </bex:Vorgang>'
    myBody += '     </soapenv:Body>'
    myBody += '</soapenv:Envelope>'
    return myBody

def erstelleFall(partner_id, api_key):
    XMLresponse = requests.post(url, data=makeBody(partner_id, api_key))
    print(XMLresponse.content)
    #response = xmltodict.parse(XMLresponse.content, process_namespaces=True, namespaces={'www.europace2.de/baufiSmart/bex/schema/bex-v13-VorgangAnlegen':None})
    response = XMLresponse.content
    successful=True
    return response, successful
