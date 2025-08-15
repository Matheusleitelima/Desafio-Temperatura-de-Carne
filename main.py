
def medir_temperatura(calcular_temperatura):

    if calcular_temperatura < 48:
        print('Necessario cozinhar mais')

    elif calcular_temperatura >= 48  and calcular_temperatura < 54:
        print('Selada')

    elif calcular_temperatura >= 54 and calcular_temperatura < 60:
        print('Ao ponto para o mal')

    elif calcular_temperatura >= 60 and calcular_temperatura < 65:
        print('Ao ponto')

    elif calcular_temperatura >= 65 and calcular_temperatura < 71:
        print('Ao ponto para o bem')

    elif calcular_temperatura >= 71:
        print('Bem passada')

temperatura_user = int(input('Qual a temperatura da carne?'))
medir_temperatura(temperatura_user)




