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
    # Prueba exitosa en la opcion 1
    

elif opcion == "2" :
    conversor_variable("argentinos", 99.01)
    # 99.01
    # Prueba exitosa en la opcion 2 

elif opcion == "3" : 
    conversor_variable("mexicanos",20.88)
    #20.88
    # Prueba exitosa en la opcion 3

else :
    print("E R R O R Favor de ingresar una opción valida, reinicie el programa de nuevo")


