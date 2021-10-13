menu = """
Bienvenidos al conversor de monedas 💰

Seleccione su moneda de origen:

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elije una opción: """

opcion = int(input(menu))

if opcion == 1 :
    pesos_colombianos = input("Cuantos pesos colombianos tienes?: ")
    pesos_colombianos = float(pesos_colombianos)
    valor_dolar = 3752.46
    dolares = pesos_colombianos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2 :
    pesos_argentinos = input("Cuantos pesos argentinos tienes?: ")
    pesos_argentinos = float(pesos_argentinos)
    valor_dolar = 99.01
    dolares = pesos_argentinos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3 : 
    pesos_mexicanos = input("Cuantos pesos mexicanos tienes?: ")
    pesos_mexicanos = float(pesos_mexicanos)
    valor_dolar = 20.88
    dolares = pesos_mexicanos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else :
    print("E R R O R Favor de ingresar una opción valida")

    opcion = int(input(menu))

