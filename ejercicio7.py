numerosGanadores = []

for i in range(1,6):
    numero = int(input("Ingrese el numero "+str(i)+" ganador "))
    numerosGanadores.append(numero)

numerosGanadores.sort(reverse=False)
print("Los numeros ganadores son: " + str(numerosGanadores))
