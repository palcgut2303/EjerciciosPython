from typing import List

lista = ["Matematicas","Fisica", "Química", "Historia", "Lengua"]
notas = []
for palabra in range(len(lista)):
    nota = int(input("Nota en "+ lista[palabra]+" : "))
    notas.append(nota)

    
for i in range(len(lista)):
    print("Has sacado en " + lista[i] + " : " + str(notas[i]))