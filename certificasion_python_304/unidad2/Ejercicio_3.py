#Programa para mostrar el abecedario uando una matris
Abecedario = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "Ñ"],
    ["O", "P", "Q", "R", "S"],
    ["T", "U", "V", "w", "x"],
    ["y", "z", "", "", ""]
]

print("ABECEDARIO EN UNA MATRIZ")
print("------------------------")

for fila in abecedario:
    for letra in fila:
        if letra != "":
            print(letra, end=" ")
    print()        
    