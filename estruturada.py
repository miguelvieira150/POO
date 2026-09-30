nomes = []
notas1 = []
notas2 = []

def cadastrar():
    nomes = input('Nome do estudante:')
    notas1 = float(input('notas1:'))
    notas2 = float(input('notas2:'))

    nomes.append(nomes)
    notas1.append(notas1)
    notas2.append(notas2)
    print('Estudante cadastrado.')

def calcular_media(indice):
    return (notas1 [indice] + notas2[indice]) /2

def situacao(indice):
    media = calcular_media(indice)
    if media >= 6:
        return 'Aprovado'   
    elif media >= 4:
        return 'Recuperção'
    return 'Reprovado'

def listar():
    if len(nomes) == 0:
        print('Nenhum estudante cadastrado.')
        return

    print(f'\n{'NOME':<16}{'N1':<7}{'N2':<7}{'MÉDIA':<8}{'SITUACAO':<14}')

    for i in range (len(nomes)):
        print(f'{nomes[i]:<16}{notas1[i]:<7}{notas2[i]:<7}'f'{calcular_media(i):<8.1f}{situacao(i):<14}')

def media_da_turma():
    if len(nomes) == 0:
        print('Nenhum estudante cadastrado.')
        return

    soma = 0
    for i in range(len(nomes)):
        soma = soma + calcular_media(i)
        print(f'\nMédia da turma: {soma/len(nomes):.2f}')

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