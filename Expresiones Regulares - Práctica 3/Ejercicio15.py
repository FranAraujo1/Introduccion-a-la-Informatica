import re
mail = input("Dame el mail:")
patron = '^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z\.)]{2,15}$'
    
def ingresar_mail(email):
    if re.search(patron, email) is not None:
        print("La dirección", email,"es válida")
    else:
        print("La dirección",email,"no es válida")
ingresar_mail(mail)