dolares = input("Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_peso = 0.048
pesos = dolares / valor_peso
pesos = round(pesos,2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos") 