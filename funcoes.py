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
    
    arquivo = open("cadastros.csv", "a")
    arquivo.write(clinica + "," + nome + "," + idade + "," + sintoma + "\n")
    arquivo.close()
    return "Paciente cadastrado!"

def exibir_pacientes():
    return cadastros

def remover_paciente(nome,clinica):
    encontrado = False
    for k in range(len(cadastros)):
        if cadastros[k][1].lower() == nome.lower() and cadastros[k][0].lower() == clinica.lower():
            encontrado = True 
            del cadastros[k]
            break
    if encontrado == True:
        arquivo = open("cadastros.csv", "w")
        for paciente in cadastros:
            arquivo.write(paciente[0] + "," + paciente[1] + "," + paciente[2] + "," + paciente[3] +"\n")
        arquivo.close()
        return "Paciente removido da lista de cadastros."
    else: 
        return "Paciente não encontrado."

def buscar_paciente_nome(clinica,nome):
    encontrado = False
    for l in range(len(cadastros)):
        if cadastros[l][1].lower() == nome.lower() and cadastros[l][0].lower() == clinica.lower() :
            encontrado = True 
            print(cadastros[l])
    if encontrado == False: 
        return "Paciente não encontrado."

def buscar_pacientes_sintoma(sintoma,clinica):
    encontrado = False 
    for g in range(len(cadastros)):
        if cadastros[g][3].lower() == sintoma.lower() and cadastros[g][0].lower() == clinica.lower() :
            encontrado = True 
            print(cadastros[g])
    if encontrado == False:
        return "Paciente não encontrado."

def buscar_pacientes_clinica(clinica):
    encontrado = False
    for h in range(len(cadastros)):
        if cadastros[h][0].lower() == clinica.lower() :
            encontrado = True 
            print(cadastros[h])
    if encontrado == False:
        return "Paciente não encontrado."

def alterar_sintoma(nome, novo_sintoma,clinica):
    encontrado = False 
    for y in range(len(cadastros)):
        if cadastros[y][1].lower() == nome.lower() and cadastros[y][0].lower() == clinica.lower():
            encontrado = True 
            cadastros[y][3] = novo_sintoma
    if encontrado == True:
        return "Sintoma alterado."
    else:
        return "Paciente não encontrado."