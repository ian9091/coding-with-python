#Reto imprimir todas las potencias de 2 hasta mil



def run(num,rept):
    if num <= rept:
        contador = num
        print('2 Elevado a ' + str(contador) + ' es igual a ' + str(2**contador))
        run(num+1,rept)
    
    else: 
        print('Fin')
    

if __name__ == '__main__':
    limite = int(input('Escriba el limite de la potencia de 2: '))
    run(0,limite)
