'''
Exercício de Inteligência Computacional - Ciência de Dados FATEC Santana de Parnaíba - 4º Semestre
Agente inteligente robô aspirador
Autor: Alef Matias
'''

from random import randint
import time

print('*** SETORES ***')
setores = {'a0': randint(0, 1),
           'z7': randint(0, 1),
           'y2': randint(0, 1),
           'h12': randint(0, 1),
           'w4': randint(0, 1),
           'a5': randint(0, 1),
           'p3': randint(0, 1),
           'd7': randint(0, 1),
           'g8': randint(0, 1),
           'j10': randint(0, 1),
           'z0': randint(0, 1),
           'a7': randint(0, 1),
           'y28': randint(0, 1),
           'q12': randint(0, 1),
           'u4': randint(0, 1),
           'a10': randint(0, 1),
           'p9': randint(0, 1),
           'e7': randint(0, 1),
           'k8': randint(0, 1),
           'j5': randint(0, 1)
           }

for chave, valor in setores.items():
    if valor == 0:
        setores[chave] = 'limpo'
    else:
        setores[chave] = 'sujo'

for chave, valor in setores.items():
    print(f'{chave} - {valor}')

print('\n')

for chave, valor in setores.items():
    if valor == 'sujo':
        print(f'O setor {chave} está {valor}')

print('\n')

while True:
    opcao = str(input('Limpar os setores? (s/n): ')).lower()
    if opcao == 's':
        print('Iniciando limpeza...\n')
        for chave, valor in setores.items():
            if valor == 'sujo':
                setores[chave] = 'limpo'
                print(f'Limpando setor {chave}...')
                time.sleep(1)
                print(f'Setor {chave} limpo')
                time.sleep(1)
        break
    elif opcao == 'n':
        print('Ok, processo finalizado...')
        break
