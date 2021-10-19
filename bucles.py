#Este programa permite calcular las potencias de 2 hasta el 
#resultado que definamos al inicio del programa. 

def operacion(cont):
    return 2**cont

def mensaje(cont,oper):
    print('2 Elevado a ' + str(cont) + ' es igual a ' + str(oper))

def bucle(contador,limite):
    if operacion(contador) <= limite:
        mensaje(contador,operacion(contador))
        bucle(contador+1,limite)
    else: 
        print('Fin')

def run():
    limite = int(input('Escriba el limite de la potencia de 2: '))
    contador = 0
    print('2 elevado a ' + str(contador) + ' es igual a ' + str(2**contador))
    bucle(contador+1,limite)


if __name__ == '__main__':
    run()
