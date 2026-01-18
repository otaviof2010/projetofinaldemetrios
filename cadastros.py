import csv
from rich.console import Console
console = Console()
conteudo = []

def exibir_pacientes():
    
    cadastros = open("cadastros.csv", "r")
    conteudo = cadastros.read()
    cadastros.close()
    if conteudo == "":
        console.print ("[bold white]Não existem pacientes cadastrados ainda! [/bold white]")
    else:
        console.print(f"[bold white]os pacientes já cadastrados são:\n{conteudo} [/bold white]")

def cadastrar_paciente(nome,idade,sintoma):
    cadastros = open("cadastros.csv", "a")
    cadastros.write(nome + "," + idade + "," + sintoma + "\n")
    cadastros.close()

def remover_paciente(nome_remove,encontrado):
    cadastros = open("cadastros.csv", "r")
    busca = nome_remove +","
    linhas = cadastros.readlines()
    cadastros.close()
    cadastros = open("cadastros.csv", "w")
    
    for i in range(len(linhas)):
        if busca not in linhas[i]:
            cadastros.write(linhas[i])
        else:
            encontrado = True
        
    if encontrado == True:
        console.print (f"[blue] O paciente {nome_remove} foi removido da lista de cadastros.[/blue]")
    else:
        console.print (f"[blue] O paciente {nome_remove} não foi encontrado.[/blue]")
    
    cadastros.close()
    
def alterar_sintoma(nome, novo_sintoma):
    cadastros = open("cadastros.csv", "r")
    linhas = cadastros.readlines()
    cadastros.close()

    cadastros = open("cadastros.csv", "w")
    busca = nome.lower() + ","
    encontrado = False
    for w in range(len(linhas)):
        if busca in linhas[w].lower():
            nova_linha = ""
            i = 0
            virgulas = 0
            while i < len(linhas[w]):
                nova_linha += linhas[w][i]
                if linhas[w][i] == ",":
                    virgulas += 1
                if virgulas == 2:
                    break
                i += 1
                
            cadastros.write(nova_linha + novo_sintoma + "\n")
            encontrado = True
        else: 
            cadastros.write(linhas[w])
        
    cadastros.close()
    if encontrado == True:
        console.print("[blue]Sintoma alterado.[/blue]") 
    else: 
        console.print("[blue]Paciente não encontrado.[/blue]") 





def menu():
    cadastros = open("cadastros.csv", "r")
    console.print('[bold red]Menu de Navegação[/bold red]')
    console.print('[dark_red]1.exibir pacientes[/dark_red]')
    console.print('[dark_red]2.cadastrar[/dark_red]')
    console.print('[dark_red]3.remover paciente[/dark_red]')
    console.print('[dark_red]4.alterar sintoma[/dark_red]')
    console.print('[dark_red]5.sair[/dark_red]')
    cadastros.close()
    
    op = int(input('escolha uma opção '))
    console.print (f"[blue]opção escolhida foi {op}[/blue]")
    return op
    
while True:
    opção = menu()
    if opção == 1:
        
        exibir_pacientes()
    elif opção == 2:
        nome = input("nome:")
        idade = input('idade:')
        sintoma = input('sintoma:')
        
        cadastrar_paciente(nome,idade,sintoma)
        console.print ("[blue]Paciente cadastrado![/]")
    elif opção == 3:
        nome_remove = input('Digite o nome que deseja remover: ')
        encontrado = False
        remover_paciente(nome_remove,encontrado)
        
    elif opção == 4:
        nome = input('escreva o nome do paciente')
        novo_sintoma = input('escreva o sintoma q vc quer alterar')
        alterar_sintoma(nome, novo_sintoma)

    elif opção == 5:
        console.print("[bold white]Saindo do sistema...[/bold white]")

        break
    else:
        console.print("[bold red]Opção inválida![/bold red]")

        