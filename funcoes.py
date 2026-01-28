import csv
arquivo = open("cadastros.csv", "r")
linhas = arquivo.readlines()
cadastros = []
for i in range (len(linhas)):
    linha = []
    texto = ""
    for j in range (len(linhas[i])):
        if linhas[i][j] != "," and linhas[i][j] != "\n":
            texto += linhas[i][j]
        else:
            linha.append(texto)
            texto = ""
    cadastros.append(linha)
arquivo.close()

def cadastrar_paciente (clinica, nome, idade, sintoma):
    novo_paciente = [clinica, nome, idade, sintoma]
    cadastros.append(novo_paciente)
    print ("Paciente cadastrado!")

def exibir_pacientes():
    for j in range (len(cadastros)):
        print(cadastros[j])

def remover_paciente(nome,clinica):
    encontrado = False
    for ç in range(len(cadastros)):
        if cadastros[ç][1].lower() == nome.lower() and cadastros[ç][0].lower() == clinica.lower():
            encontrado = True 
            del cadastros[ç]
    if encontrado == True:
        print("Paciente removido da lista de cadastros.")
    else: 
        print("Paciente não encontrado.")

def buscar_paciente_nome(clinica,nome):
    encontrado = False
    for l in range(len(cadastros)):
        if cadastros[l][1].lower() == nome.lower() and cadastros[l][0].lower() == clinica.lower() :
            encontrado = True 
            print(cadastros[l])
    if encontrado == False: 
        print("Paciente não encontrado.")

def buscar_pacientes_sintoma(sintoma):
    encontrado = False 
    for g in range(len(cadastros)):
        if cadastros[g][3].lower() == sintoma.lower():
            encontrado = True 
            print(cadastros[g])
    if encontrado == False:
        print("Paciente não encontrado.")

def buscar_pacientes_clinica(clinica):
    encontrado = False
    for h in range(len(cadastros)):
        if cadastros[h][0].lower() == clinica.lower() :
            encontrado = True 
            print(cadastros[h])
    if encontrado == False:
        print("Paciente não encontrado.")

def alterar_sintoma(nome, novo_sintoma):
    encontrado = False 
    for y in range(len(cadastros)):
        if cadastros[y][1].lower() == nome.lower():
            encontrado = True 
            cadastros[y][3] = novo_sintoma
    if encontrado == True:
        print("Sintoma alterado.")
    else:
        print("Paciente não encontrado.")