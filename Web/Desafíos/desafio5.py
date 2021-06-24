import requests
#r = requests.get('https://macowins-server.herokuapp.com/prendas')
#r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=pantalon')
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=saco')
r = requests.get('https://macowins-server.herokuapp.com/ventas')

r.json()
r.content

