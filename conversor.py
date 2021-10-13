menu = """
Bienvenidos al conversor de monedas 💰

Seleccione su moneda de origen:

1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elije una opción: """

def conversor_variable(nacionalidad,valor_dolar_variable):
    pesos = input("Cuantos pesos " + nacionalidad + " tienes?: ")
    pesos = float(pesos)
    valor_dolar = valor_dolar_variable
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

opcion = input(menu)

if opcion == "1" :
    conversor_variable("colombianos",3752.46)
    # 3752.46
    # Se realiza la prueba conla opción 1 esta sección del codigo,  
    # el resto del aun corre.

elif opcion == "2" :
    pesos_argentinos = input("Cuantos pesos argentinos tienes?: ")
    pesos_argentinos = float(pesos_argentinos)
    valor_dolar = 99.01
    dolares = pesos_argentinos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
    # 99.01

elif opcion == "3" : 
    pesos_mexicanos = input("Cuantos pesos mexicanos tienes?: ")
    pesos_mexicanos = float(pesos_mexicanos)
    valor_dolar = 20.88
    dolares = pesos_mexicanos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
    #20.88

else :
    print("E R R O R Favor de ingresar una opción valida, reinicie el programa de nuevo")


