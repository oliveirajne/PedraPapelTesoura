# importando modulo para utilizar o random
from random import randint

# variaveis
contador          = 0
jogada_computador = 0
jogada_player     = 1
aux               = 0
aux_vc            = 0
aux_pc            = 0
aux_empate        = 0

# no vetor, o valor 0 significa empate, 1 para jogador e 2 para computador
v_resultados = []

# funcoes
def jogada():
    aux = int(input("Digite 1 para papel, 2 para pedra e 3 para tesoura: "))
    return aux

# calcula reultado da jogada
def resultado_jogada(jogada_player):
    if jogada_player == 1:
        if jogada_computador == 2:
            print('Voce venceu!')
            v_resultados.append(1)
        if jogada_computador == 3:
            print('Computador venceu!')
            v_resultados.append(2)
        else:
            print('Empate.')
            v_resultados.append(0)
    if jogada_player == 2:
        if jogada_computador == 1:
            print('Computador venceu.')
            v_resultados.append(2)
        if jogada_computador == 3:
            print('Voce venceu!')
            v_resultados.append(1)
        else:
            print('Empate.')
            v_resultados.append(0)
    if jogada_player == 3:
        if jogada_computador == 1:
            print('Voce venceu!')
            v_resultados.append(1)
        if jogada_computador == 2:
            print('Computador venceu.')
            v_resultados.append(2)
        else:
            print('Empate.')
            v_resultados.append(0)

# mostra resultado final
def resultado_final(aux_vc, aux_pc, aux_empate):
    aux = 0
    while(aux < contador - 1):
        if v_resultados[aux] == 1:
            aux_vc += 1
        if v_resultados[aux] == 2:
            aux_pc += 1
        else:
            aux_empate += 1
        aux += 1
    if contador > 1:
        print('Porcentagem de partidas em que voce venceu: ' + str(aux_vc * 100 / (contador - 1)))
        print('Porcentagem de empates: ' + str(aux_empate * 100 / (contador - 1)))
        print('Porcentagem pc: ' + str(aux_pc * 100 / (contador -1)))

    print('quantidade de jogadas : ' + str(contador - 1))
    print('FIM DE JOGO')

while jogada_player > 0 and jogada_player < 4:

    jogada_player     = jogada()
    jogada_computador = randint(1,3)

    print('Jogada do computador: ' + str(jogada_computador))

    resultado_jogada(jogada_player)
    contador += 1

# termina o jogo e imprime a quantidade de jogadas
resultado_final(aux_vc, aux_pc, aux_empate)
