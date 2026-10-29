#Creando un diccionario
persona={
    "Nombre":"Luis",
    "Edad":41,
    "Profecion":"Ingeniero",
    "Estudiante":False
}
print(persona)
#Accediendo a un valor en especifico
print(persona["Nombre"])
print(persona.get("Profecion"))
persona["Edad"]=43
print(persona["Edad"])