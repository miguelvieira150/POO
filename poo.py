from estruturada import menu


class Estudante:

    def __init__(self,nome,nota1,nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2 

    def media(self):
        return (self.nota1 + self.nota2) / 2

    def situacao(self):
        if self.media() >= 6:
            return 'aprovado'
        elif self.media() >= 4:
            return 'recuperacao'

        return 'reprovado'

def descrever(self):
    return (f'{self.nome <16}{self.nota1:<7}{self.nota2:<7}'f'{self.media():<8.1f}{self.situacao():<14}')

estudantes = []

def cadastrar():
    nome = input('Nome do estudante:')
    nota1 = float(input('nota1: '))
    nota2 = float(input('nota2: '))

    estudantes.append(estudantes(nome,nota1,nota2))
    print('Estudante cadastrado.')

def listar():
    if len(estudantes) == 0:
        print('nenhum estudante cadastrado')
        return
    print(f'\n{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUACAO':<14}')
    for estudante in estudantes:
        print(estudantes.descrever())

def media_da_turma():
    if len(estudantes) ==0:
        print('nenhum estudante cadastrado.')
        return

    soma == 0

    for estudante in estudantes:
        soma = soma + estudante.media()

    print(f'\nMedia da turma: {soma/len(estudantes):.2f}')

def menu():
    while True:
        print('\n1 - cadastrar estudante')
        print('2 - Listar estudante')
        print('3 - Média da turma')
        print('0 - Sair')

        opcao = input('Opção: ')

        if opcao == '1':
            cadastrar()
        elif opcao == '2':
            listar()
        elif opcao == '3':
            media_da_turma()
        elif opcao == '0':
            break
        else:
            print('Opção inválida.')

menu()