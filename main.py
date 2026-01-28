import funcoes
from rich import print


def menu():    
    print('[bold red]Menu de Navegação[/bold red]')
    print('[dark_red]1.exibir pacientes[/dark_red]')
    print('[dark_red]2.cadastrar[/dark_red]')
    print('[dark_red]3.remover paciente[/dark_red]')
    print('[dark_red]4.alterar sintoma[/dark_red]')
    print('[dark_red]5.buscar paciente por nome[/dark_red]')
    print('[dark_red]6.buscar pacientes por clinica[/dark_red]')
    print('[dark_red]7.buscar pacientes por sintoma[/dark_red]')
    print('[dark_red]8.sair[/dark_red]')
    op = int(input('escolha uma opção '))
    print (f'[italic bold white] opção escolhida:{op} [/italic bold white]')
    return op

while True:
    opcao = menu()

    if opcao == 1:
        
        print(funcoes.exibir_pacientes())
        
    elif opcao == 2:
        clinica = input('clinica: ')
        nome = input("nome: ")
        idade = input('idade: ')
        sintoma = input('sintoma: ')
        print(funcoes.cadastrar_paciente (clinica, nome, idade, sintoma))
        

    elif opcao == 3:
        nome = input('escreva o nome do paciente q vc quer remover ')
        clinica = input('escreva a clinica do paciente q vc quer remover ')
        print(funcoes.remover_paciente(nome,clinica))
        
    elif opcao == 4:
        nome = input('escreva o nome do paciente ')
        novo_sintoma = input('escreva o sintoma q vc quer alterar ')
        clinica = input('escreva a clinica ')
        print(funcoes.alterar_sintoma(nome,novo_sintoma,clinica))

    elif opcao == 5:
        nome = input('escreva o nome do paciente ')
        clinica = input('escreva a clinica ')
        
        print(funcoes.buscar_paciente_nome(clinica,nome))

    elif opcao == 6:
        clinica = input('escreva a clinica ')
        
        print(funcoes.buscar_pacientes_clinica(clinica))
    
    elif opcao == 7:
        sintoma = input('escreva o sintoma ')
        clinica = input('escreva a clinica ')
        print(funcoes.buscar_pacientes_sintoma(sintoma,clinica))

    elif opcao == 8:
        print("[bold white]Saindo do sistema...[/bold white]")
        break
    else:
        print("[bold red]Opção inválida![/bold red]")

        