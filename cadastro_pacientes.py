'''
Exercício - Cadastro de Pacientes
Autor: Alef Henrique Aparecido Costa Matias
'''

class Paciente():
    def __init__(self):
        self.lista = []

    def length(self):
        return len(self.lista)

    def empty(self):
        return self.length() == 0

    def showData(self):
        print(self.lista)

    def insert(self, nome, rg, telefone, email, instagram):
        self.lista.append(nome)
        self.lista.append(rg)
        self.lista.append(telefone)
        self.lista.append(email)
        self.lista.append(instagram)

    def delete(self, data):
        if data in self.lista:
            self.lista.remove(data)
            print(f'{data} apagado com sucesso!')
        else:
            print('Não há esse dado na lista!')

    def search(self, data):
        if data in self.lista:
            print(f'{data} foi localizado(a) e está na {self.lista.index(data)}ª posição da lista!')
        else:
            print('Não existe este dado na lista!')

paciente = Paciente()

print('='*18)
print('LISTA DE PACIENTES')
print('='*18)

# Menu sempre será exibido após uma ação
while True:
    print('\n1 - Cadastrar um paciente;')
    print('2 - Listar os pacientes cadastrados;')
    print('3 - Excluir um dado da lista;')
    print('4 - Consultar um dado na lista;')
    print('5 - Sair.')

# Aceitando apenas números inteiros
    while True:
        try:
            option = int(input('\nO que deseja fazer? '))
            break
        except:
            print('Caracter inválido! Digite apenas números inteiros!')
            continue

# Restringindo as opções
    if option not in range(1,6):
        print(f'{option} não está dentro do intervalo!')

    elif option == 1:
        # Aceitando apenas número inteiros
        while True:
            try:
                n = int(input('\nQuantos pacientes deseja cadastrar? '))
                break
            except:
                print('Caracter inválido! Digite apenas números inteiros!')
                continue

        if n == 0:
            print('Nenhum paciente será cadastrado. Voltando ao menu principal...')
            continue

        for i in range(n):
            nome = input('Nome: ').upper().strip()
            rg = input('RG: ').upper().strip()
            telefone = input('Telefone: ').upper().strip()
            email = input('E-mail: ').upper().strip()
            instagram = input('Instagram: ').upper().strip()

            paciente.insert(nome, rg, telefone, email, instagram)

        print('\nPaciente(s) cadastrado(s) com sucesso!')

    elif option == 2:
        if paciente.empty() == True:
            print('Ainda não há pacientes cadastrados.')
        else:
            print('Pacientes cadastrados:')
            paciente.showData()

    elif option == 3:
        data = input('Qual dado deseja apagar? ')
        paciente.delete(data.upper().strip())

    elif option == 4:
        data = input('Qual dado deseja buscar? ')
        paciente.search(data.upper().strip())

    elif option == 5:
        print('Saindo...')
        break
