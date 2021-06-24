import requests

r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera')

r.json()
r.content