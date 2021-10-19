#Reto imprimir todas las potencias de 2 hasta mil

def mensaje(cont,oper):
    print('2 Elevado a ' + str(cont) + ' es igual a ' + str(oper))

def run():
    limite = int(input('Escriba el limite de la potencia de 2: '))
    contador = 0
    operacion = 2**contador
    
    if operacion <= limite:
        mensaje(contador,operacion)
        mensaje(contador+1,operacion)
    
    else: 
        print('Fin')
    

if __name__ == '__main__':
    run()
