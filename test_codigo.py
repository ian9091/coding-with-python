def run():
    numeros=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113]
    entrada=int(input('Ingrese un número para evaluar: '))
    for numero in numeros:
        resultado = entrada/numero
        #print ('comprobando la operacion')
        #print (str(entrada)+' dividido en '+str(numero)+' es: '+str(resultado))
        if entrada%numero==0:
            print ('No es primo')
            break
        if resultado<=numero:
            print ('hasta aquí validé,Es primo')
            break


if __name__=='__main__':
    run()