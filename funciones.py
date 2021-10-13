#def mensaje_especial():
 #   print("Mensaje especial ")
  #  print(" ¡Estoy aprendiendo a usar funciones! ")

#mensaje_especial()

def conversacion(mensaje):
    print("Hola")
    print("como estas")
    print(mensaje)
    print("adios")

opcion = input("Elige una opción (1, 2, 3): ")
if opcion == "1":
    conversacion("Elegiste la opcion 1")
elif opcion == "2":
    conversacion("Elegiste la opcion 2")
elif opcion == "3":
    conversacion("Elegiste la opcion 3")
else:
    print("Elige una opcion correcta")
