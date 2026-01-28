import funcoes
import csv
from rich.console import Console
console = Console()


def menu():
    cadastros = open("cadastros.csv", "r")
    console.print('[bold red]Menu de Navegação[/bold red]')
    console.print('[dark_red]1.exibir pacientes[/dark_red]')
    console.print('[dark_red]2.cadastrar[/dark_red]')
    console.print('[dark_red]3.remover paciente[/dark_red]')
    console.print('[dark_red]4.alterar sintoma[/dark_red]')
    console.print('[dark_red]5.buscar pacientes por clinica[/dark_red]')
    console.print('[dark_red]6.buscar pacientes por sintoma[/dark_red]')
    console.print('[dark_red]7.sair[/dark_red]')
    cadastros.close()
    
    op = int(input('escolha uma opção '))
    console.print (f"[blue]opção escolhida foi {op}[/blue]")
    return op
    
while True:
    opção = menu()
    if opção == 1:
        
        print(funcoes.exibir_pacientes())
        
    elif opção == 2:
        nome = input("nome:")
        idade = input('idade:')
        sintoma = input('sintoma:')
        clinica = input('clinica:')

        print(funcoes.cadastrar_paciente (clinica, nome, idade, sintoma))

        console.print ("[blue]Paciente cadastrado![/]")
    elif opção == 3:
        nome = input('escreva o nome do paciente q vc quer remover ')
        clinica = input('escreva a clinica do paciente q vc quer remover ')
        print(funcoes.remover_paciente(nome,clinica))
        
    elif opção == 4:
        nome = input('escreva o nome do paciente ')
        novo_sintoma = input('escreva o sintoma q vc quer alterar ')
        print(funcoes.alterar_sintoma(nome,novo_sintoma))

    elif opção == 5:
        nome = input('escreva o nome do paciente ')
        clinica = input('escreva a clinica ')
        
        print(funcoes.buscar_paciente_nome(clinica,nome))

    elif opção == 6:
        clinica = input('escreva a clinica ')
        
        print(funcoes.buscar_pacientes_clinica(clinica))
    
    elif opção == 7:
        sintoma = input('escreva o sintoma ')
        print(funcoes.buscar_pacientes_sintoma(sintoma))

    elif opção == 8:
        console.print("[bold white]Saindo do sistema...[/bold white]")

        break
    else:
        console.print("[bold red]Opção inválida![/bold red]")

        