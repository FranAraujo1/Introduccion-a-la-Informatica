import re 
string = "pl@t@ d& c@mid&"
patron = "[@&](.*?)[@&]"
lista = re.findall(patron, string)
print(lista)
for i in lista: 
    print(str(i) + str(re.search(i, string). span())
