#Este programa permite calcular las potencias de 2 hasta el 
#resultado que definamos al inicio del programa. 
#Usando el cicle while

def run():
    LIMITE = int(input('Escriba el limite de la potencia de 2: '))
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print('2 elevado a ' + str(contador) + ' es igual a ' + str(2**contador))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == '__main__':
    run()
