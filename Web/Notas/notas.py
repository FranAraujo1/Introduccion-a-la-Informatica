import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
r.json()
r.json()['id']
r.json()['tipo']
r.headers
type(r.headers)
r.headers['Content-Type']
r.headers['Date']
r.status_code

