def es_primo(numero):
    primos = [2,3,5,7,11,13]
    
    for i in primos:
        resultado = numero/i
        if numero % i == 0:
            return False
            break
        if resultado <= numero:
            return True
            break
        

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else: 
        print('No es primo')

if __name__ == '__main__' :
    run()
