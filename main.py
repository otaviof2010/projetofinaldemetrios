import funcoes
from rich import print



def menu():
    print('[bold blue]Menu de Navegacao[/]')
    print('[dark_blue]1.Exibir pacientes[/]')
    print('[dark_blue]2.Cadastrar[/]')
    print('[dark_blue]3.Remover paciente[/]')
    print('[dark_blue]4.Alterar sintoma[/]')
    print('[dark_blue]5.Buscar paciente por nome[/]')
    print('[dark_blue]6.Buscar pacientes por clinica[/]')
    print('[dark_blue]7.Buscar pacientes por sintoma[/]')
    print('[dark_blue]8.Sair[/]')
    op = int(input('Escolha uma opção: '))
    print (f'[italic bold white] Opção escolhida: {op} [/italic bold white]')
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
        nome = input('Escreva o nome do paciente que você quer remover: ')
        clinica = input('Escreva a clínica do paciente que você quer remover: ')
        print(funcoes.remover_paciente(nome,clinica))
        
    elif opcao == 4:
        nome = input('Escreva o nome do paciente: ')
        novo_sintoma = input('Escreva o novo sintoma: ')
        clinica = input('Escreva a clínica: ')
        print(funcoes.alterar_sintoma(nome,novo_sintoma,clinica))

    elif opcao == 5:
        nome = input('Escreva o nome do paciente: ')
        clinica = input('Escreva a clínica: ')
        print(funcoes.buscar_paciente_nome(clinica,nome))

    elif opcao == 6:
        clinica = input('Escreva a clínica: ')
        print(funcoes.buscar_pacientes_clinica(clinica))
    
    elif opcao == 7:
        sintoma = input('Escreva o sintoma: ')
        clinica = input('Escreva a clinica: ')
        print(funcoes.buscar_pacientes_sintoma(sintoma,clinica))

    elif opcao == 8:
        print("[bold white]Saindo do sistema...[/bold white]")
        break
    else:
        print("[bold red]Opcao invalida![/bold red]")
    
    
