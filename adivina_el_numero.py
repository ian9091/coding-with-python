import random

def run():
    numero_random = random.randint(1,100)

    numero_elegido = int(input('Elige un numero entre el 1 y el 100: '))
    creditos = 5
    while numero_elegido != numero_random:
        if numero_elegido < numero_random:
            print('Elige un numero mayor')
            creditos -= 1
        else:
            print('Busca un numero más pequeño')
            creditos -= 1
        if creditos == 0:
            break
        numero_elegido = int(input('Elige otro número: '))


    print('¡Ganaste!')


if __name__ == '__main__':
    run()