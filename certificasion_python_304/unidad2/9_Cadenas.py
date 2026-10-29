Cadena1='Hola'
Cadena2='Mundo'
multilinea="""Esto es una cadena
de varias lineas"""
print(Cadena1 + Cadena2 + multilinea)#print(f"{cadena1}")
#cadenas y repeticion
eco="ja"*3
print(eco)
#Cambiar una cadena de minuscula a mayuscula
tu_nombre='Carlos'
print(tu_nombre.upper())
#Cambiar una cadena de mayuscula a minuscula 
print(tu_nombre.lower())
#Remplazar texto en una cadena
frase="Me gusta programacion"
print(frase.replace("programacion","matematicas")) 
#Formato de cadenas (F-string)
edad=16
Nombre='Luis'
mensaje=f"Hola, me llamo {Nombre} y tengo\n{edad} años"
print(mensaje)
#Contar los caracteres de una cadena
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#Comprobar si un texto contiene una palabra
oracion="Agregar python es divertido"
if "java" in oracion:
    print("Encontrado")
else:
 print("No esta")
#Validar contenido de una cadena
nlista="Luis"
#print(nlista.is_integer())
print(nlista.isalpha())
print(nlista.isdigit())
