# Trabalho urna
# Aluno: Luan Patrick Medeiros Alves
# Disciplina: Construção de Algoritimos
# Semestre: 1

eleitores = int(input('Digite a quantidade de eleitores que vão participar: '))
count = 0

votoVincent = 0
votoJules = 0
votoMarsellus = 0

while count < eleitores:
    candidato1 = 'Vincent Vega'
    candidato2 = 'Jules Winnfield'
    candidato3 = 'Marsellus Wallace'

    voto = int(input(('''
       ~> Olá, Seja bem vindo(a) à Urna Eletrônica!

  - Digite um dos números abaixo para votar em seu respectivo candidato:

( 1 ) Vincent Vega
( 2 ) Jules Winnfield
( 3 ) Marsellus Wallace

============================================

    ''')))

    tentativa = 0
    valido = 0

    while (valido != 1 and tentativa <= 3):
        if voto == 1:
            valido   = 1
            print('')
            print('============================================')
            print('')
            print(f'Voto confirmado para {candidato1}!')
            votoVincent += 1
            print('')
            print('============================================')
            print('')
        elif voto == 2:
            valido = 1
            print('')
            print('============================================')
            print('')
            print(f'Voto confirmado para {candidato2}!')
            votoJules += 1
            print('')
            print('============================================')
            print('')
        elif voto == 3:
            valido = 1
            print('')
            print('============================================')
            print('')
            print(f'Voto confirmado para {candidato3}!')
            votoMarsellus += 1
            print('')
            print('============================================')
            print('')
       
        else:
            valido = 0
            tentativa += 1
            print('')
            print('         =================== Atenção! ===================')
            print('')
            print(f'~> O voto n°{voto} é invalido! Use apenas 1, 2 ou 3 (Observação: Você já tentou {tentativa}/5 vezes!')
            print('')
            voto = int(input())

        count += 1
        
    if votoVincent > votoJules and votoVincent > votoMarsellus:
        calculoPorcentagemV = (votoVincent / eleitores) * 100
        print(f'{candidato1} está ganhando com {votoVincent} votos ({calculoPorcentagemV}%')

    elif votoJules > votoVincent and votoJules > votoMarsellus:
        calculoPorcentagemJ = (votoJules / eleitores) * 100
        print(f'{candidato2} está ganhando com {votoJules} votos ({calculoPorcentagemJ}%')

    elif votoMarsellus > votoVincent and votoMarsellus > votoJules:
        calculoPorcentagemM = (votoMarsellus / eleitores) * 100
        print(f'{candidato3} está ganhando com {votoMarsellus} votos ({calculoPorcentagemM}%')

        calculoPorcentagem = (votoVincent + votoMarsellus) / eleitores * 100
        print(f'Vincent e Marsellus empataram! Vincent com {votoVincent} votos ({calculoPorcentagem}%) e Marsellus com {votoMarsellus} votos ({calculoPorcentagem}%')
    elif votoVincent == votoJules:
        calculoPorcentagem = (votoVincent + votoJules) / eleitores * 100
        print(f'Vincent e Jules empataram! Vincent com {votoVincent} votos ({calculoPorcentagem}%) e Jules com {votoJules} votos ({calculoPorcentagem}%')
    elif votoJules == votoMarsellus:
        calculoPorcentagem = (votoJules + votoMarsellus) / eleitores * 100
        print(f'Jules e Marsellus empataram! Jules com {votoJules} votos ({calculoPorcentagem}%) e Marsellus com {votoMarsellus} votos ({calculoPorcentagem}%')

