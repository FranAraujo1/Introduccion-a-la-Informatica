import re

def caracteres_permitidos(string):
    return not bool(re.search('[^a-zA-Z0-9.]', string))

print("El string", "ABCDEFabcdef123450", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("ABCDEFabcdef123450"))
print("El string", "**&%@#!}{", "tiene todos los caracteres permitidos?")
print(caracteres_permitidos("*6%@#!}{"))