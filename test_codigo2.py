def es_primo(numero):
    for i in range(numero + 1):
        if numero == i:
            continue
        if 1 == i:
            continue
        if 0 == i:
            continue
        if numero % i == 0:
            return False
            break
        if numero % i != 0:
            return True


def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else: 
        print('No es primo')

if __name__ == '__main__':
    run()