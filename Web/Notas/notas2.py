import requests
r = requests.delete('https://macowins-server.herokuapp.com/prendas/21')
r = requests.get('https://macowins-server.herokuapp.com/prendas')
r.json()

