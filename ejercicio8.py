numeros = list(range(1, 11))

numeros_inversos = sorted(numeros, reverse=True)

for num in numeros_inversos:
    print(num, end=", ")