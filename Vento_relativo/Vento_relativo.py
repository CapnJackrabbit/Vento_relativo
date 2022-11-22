
def coleta_dados():
    flag = 0

    while flag == 0:
        rumo = int(input('Informe o rumo: '))
        if rumo > 360 or rumo < 0:
            print('Rumo informado nao e valido. Informe um valor entre 0 e 360.')
        else:
            vento = int(input('Informe a direcao do vento: '))
            if vento > 360 or vento < 0:
                print ('Vento informado nao e valido. Informe um valor entre 0 e 360.')
            else:
                flag = 1
                calcula(rumo,vento)

def continua():
    resposta = input('Deseja calcular novamente? S/N: ')
    if resposta.upper() == 'S':
        coleta_dados()
    else:
        print('\nAte a proxima!\n')


def calcula(rumo,vento):
    if rumo >= 0 and rumo <= 180:
        reciproca = rumo + 180
    else:
        reciproca = rumo - 180

    traves_direito = rumo + 90
    if traves_direito > 360:
        traves_direito -= 360

    traves_esquerdo = rumo - 90
    if traves_esquerdo < 0:
        traves_esquerdo +=360

    if rumo > 270:
        traves_direito += 360
        if vento > rumo or vento < traves_direito - 360:
            print('\nVento de proa pela direita\n')

        if vento < reciproca and vento > traves_direito - 360:
            print('\nVento de cauda pela direita')

    if rumo < 90:
        traves_esquerdo -=360
        if vento < rumo or vento > traves_esquerdo + 360:
            print('\nVento de proa pela esquerda\n')

        if vento > reciproca and vento < traves_esquerdo + 360:
            print('\nVento de cauda pela esquerda')

    if vento > rumo and vento <= traves_direito:
        print('\nVento de proa pela direita\n')
    if vento < rumo and vento >= traves_esquerdo:
        print('\nVento de proa pela esquerda\n')

    if vento > reciproca and vento < traves_esquerdo:
        print('\nVento de cauda pela esquerda\n')
    if vento < reciproca and vento > traves_direito:
        print('\nVento de cauda pela direita\n')


    if rumo in range (0,89):
        print("\nRumo: ",rumo," ","Reciproca: ", reciproca)
        print('Traves direito: ',traves_direito)
        print('Traves esquerdo:',traves_esquerdo + 360 ,'\n\n')

    elif rumo in range (271,360):
        print("\nRumo: ",rumo," ","Reciproca: ", reciproca)
        print('Traves direito: ',traves_direito - 360)
        print('Traves esquerdo:',traves_esquerdo,'\n\n')

    else:
        print("\nRumo: ",rumo," ","Reciproca: ", reciproca)
        print('Traves direito: ',traves_direito)
        print('Traves esquerdo:',traves_esquerdo,'\n\n')

    continua()


coleta_dados()