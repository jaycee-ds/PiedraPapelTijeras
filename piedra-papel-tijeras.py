from random import randint

opc = ['piedra', 'papel', 'tijeras']

ordenador = opc[randint(0,2)]

jugador = False

while jugador == False:
    jugador = input('¿Piedra, papel o tijeras? Pim, pom, ¡fuera!')

    if jugador == ordenador:
        print('¡Empate!')
    elif jugador == 'piedra':
        if ordenador == 'papel':
            print('¡Pierdes! El papel se come a la piedra')
        else:
            print('¡Ganas! La piedra parte las tijeras')
    elif jugador == 'papel':
        if ordenador == 'piedra':
            print('¡Ganas! El papel se come a la piedra')
        else:
            print('¡Pierdes! Las tijeras cortan el papel')
    elif jugador == 'tijeras':
        if ordenador == 'piedra':
            print('¡Pierdes! La piedra rompe las tijeras')
        else:
            print('¡Ganas! Las tijeras cortan el papel')
    
    jugador = False
    ordenador = opc[randint(0,2)]


