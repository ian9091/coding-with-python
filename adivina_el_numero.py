import random

def run():
    numero_random = random.randint(1,100)

    numero_elegido = int(input('Elige un numero entre el 1 y el 100: '))
    creditos = 7
    while numero_elegido != numero_random:
        if numero_elegido < numero_random:
            print('Elige un numero mayor')
            creditos -= 1
            print('Te restan ',creditos, ' creditos')
        else:
            print('Busca un numero más pequeño')
            creditos -= 1
            print('Te restan ',creditos, ' creditos')

        if creditos == 0:
            print('Se te acabaron los itentos. Fin del Juego')
            return creditos
            break
        else:
            numero_elegido = int(input('Elige otro número: '))
    if creditos != 0:
        print('Ganaste')
    


if __name__ == '__main__':
    run()