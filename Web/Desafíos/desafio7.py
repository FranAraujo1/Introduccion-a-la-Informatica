import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
r.json()
r.content
