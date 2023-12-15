lista = ["Matematicas","Fisica", "Química", "Historia", "Lengua"]
notas = []

for palabra in range(len(lista)):
    nota = int(input("Nota en "+ lista[palabra]+" : "))
    notas.append(nota)
notasSuspensas = []
asignaturasSuspensas = []
for i in range(len(notas)):
    if notas[i] < 5:
        notasSuspensas.append(notas[i])
        asignaturasSuspensas.append(lista[i])


print("Tienes que recuperar estas asignaturas: \n")

for i in range(len(asignaturasSuspensas)):
    print(asignaturasSuspensas[i] + " :" + str(notasSuspensas[i]))