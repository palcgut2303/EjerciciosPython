lista = ["Matematicas","Fisica", "Química", "Historia", "Lengua"]
notas = []

for palabra in range(len(lista)):
    nota = int(input("Nota en "+ lista[palabra]+" : "))
    notas.append(nota)
notasAprobadas = []
asignaturasAprobadas = []
for i in range(len(notas)):
    if notas[i] > 5:
        notasAprobadas.append(notas[i])
        asignaturasAprobadas.append(lista[i])



for i in range(len(lista)):
    print("Tienes que recuperar estas asignaturas: "+lista[i])