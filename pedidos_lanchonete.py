'''
Exercício - Pedidos de uma lanchonete
Autor: Alef Henrique Aparecido Costa Matias
'''

import time

class Lanchonete:
    def __init__(self):
        self.fila = []

    def length(self):
        return len(self.fila)

    def empty(self):
        return self.length() == 0

    def push(self, pedido):
        self.fila.append(pedido)

    def pop(self):
        if not self.empty():
            return self.fila.pop(0)

    def show(self):
        print(self.fila)

    def done(self):
        return self.fila[0]

    def waiting(self):
        return self.fila[1:]

pedido = Lanchonete()

print('='*19)
print('Lanchonete X-Burgão')
print('='*19)

# Carregando os pedidos na lista
while True:
    resp = str(input('Deseja cadastrar um pedido? (s/n) ').lower())
    if resp == 's':
        pedido.push(int(input('Pedido: ')))
    elif resp == 'n':
        print('Encerrando o cadastro de pedidos...')
        break
    elif resp != 's' and resp != 'n':
        print('Opção inválida! Tente novamente.')
        continue

print('\nPEDIDOS A SEREM CHAMADOS')
pedido.show()

for i in range(pedido.length()):
    print('\n')
    print(f'Pedido feito: {pedido.done()}')
    time.sleep(1)
    print(f'Próximos pedidos... {pedido.waiting()}')
    time.sleep(1)
    print(f'Encaminhado à cozinha: {pedido.done()}')
    time.sleep(1)
    print(f'Pedido concluído: {pedido.pop()}')
    time.sleep(1)

    if pedido.empty() == True:
        print('TODOS OS PEDIDOS FORAM CONCLUÍDOS!')