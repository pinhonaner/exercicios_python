# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

def perguntador(lista_perguntas):
    respostas_certas = 0
    for pergunta in lista_perguntas:
        print(pergunta['Pergunta'])
        print('')
        print('Opções: \n')
        for option in pergunta['Opções']:
            print(option)
        print('')
        resposta = input('Qual a resposta? ')
        print('')
        if resposta == pergunta['Resposta']:
            print('Parabéns, resposta certa!\n')
            respostas_certas += 1
        else:
            print('Que pena, resposta errada!\n')
    print(f'Parabéns você acertou {respostas_certas}\n')
    if respostas_certas == len(perguntas):
        print('EXCELENTE! Você acertou todas as perguntas!')

perguntador(perguntas)