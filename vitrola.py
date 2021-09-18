'''
Exercício - Vitrola
Autor: Alef Henrique Aparecido Costa Matias
'''

class Vitrola:
    def __init__(self):
        self.pilha = []

    def push(self, musicas):
        self.pilha.append(musicas)

    def pop(self):
        if not self.empty():
            return self.pilha.pop()

    def empty(self):
        return self.length() == 0

    def show(self):
        print(self.pilha)

    def next(self):
        if not self.empty():
            return self.pilha[-1]
        else:
            return 'PLAYLIST VAZIA!'

    def length(self):
        return len(self.pilha)

playlist = Vitrola()

print('='*13)
print('VITROLA FATEC')
print('='*13)

# Aceitando apenas números inteiros
while True:
    try:
        n = int(input('Quantas músicas deseja carregar? '))
        break
    except:
        print('Caracter inválido! Digite apenas números inteiros!')
        continue

# Carregando as músicas na playlist
for i in range(n):
    playlist.push(input(f'{i + 1}ª música: ').upper().strip())

print('\nPlaylist carregada')
playlist.show()

# #xecutando as músicas
for i in range(n):
    print(f'\nRestam {playlist.length()} música(s)')
    print(f'Tocando: {playlist.pop()}')
    print(f'Próxima: {playlist.next()}')

    if playlist.empty() == True:
        print("Todas as músicas foram tocadas!")
