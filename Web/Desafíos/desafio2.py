import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/400')
r.json()

r.headers
r.status_code