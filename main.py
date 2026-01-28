import funcoes
from rich import print



def menu():    
    print('[bold red]Menu de Navegacao[/bold red]')
    print('[dark_red]1.Exibir pacientes[/dark_red]')
    print('[dark_red]2.Cadastrar[/dark_red]')
    print('[dark_red]3.Remover paciente[/dark_red]')
    print('[dark_red]4.Alterar sintoma[/dark_red]')
    print('[dark_red]5.Buscar paciente por nome[/dark_red]')
    print('[dark_red]6.Buscar pacientes por clinica[/dark_red]')
    print('[dark_red]7.Buscar pacientes por sintoma[/dark_red]')
    print('[dark_red]8.sair[/dark_red]')
    op = int(input('escolha uma opcao '))
    print (f'[italic bold white] opcao escolhida:{op} [/italic bold white]')
    return op

while True:
    opcao = menu()

    if opcao == 1:
        
        print(funcoes.exibir_pacientes())
        
    elif opcao == 2:
        clinica = input('Clinica: ')
        nome = input("Nome: ")
        idade = int(input('Idade: ')) 
        sintoma = input('Sintoma: ')
        
        print(funcoes.cadastrar_paciente (clinica, nome, idade, sintoma))
        

    elif opcao == 3:
        nome = input('Escreva o nome do paciente q vc quer remover ')
        clinica = input('Escreva a clinica do paciente q vc quer remover ')
        print(funcoes.remover_paciente(nome,clinica))
        
    elif opcao == 4:
        nome = input('Escreva o nome do paciente ')
        novo_sintoma = input('Escreva o sintoma q vc quer alterar ')
        clinica = input('Escreva a clinica ')
        print(funcoes.alterar_sintoma(nome,novo_sintoma,clinica))

    elif opcao == 5:
        nome = input('Escreva o nome do paciente ')
        clinica = input('Escreva a clinica ')
        
        print(funcoes.buscar_paciente_nome(clinica,nome))

    elif opcao == 6:
        clinica = input('Escreva a clinica ')
        
        print(funcoes.buscar_pacientes_clinica(clinica))
    
    elif opcao == 7:
        sintoma = input('Escreva o sintoma ')
        clinica = input('Escreva a clinica ')
        print(funcoes.buscar_pacientes_sintoma(sintoma,clinica))

    elif opcao == 8:
        print("[bold white]Saindo do sistema...[/bold white]")
        break
    else:
        print("[bold red]Opcao invalida![/bold red]")

        