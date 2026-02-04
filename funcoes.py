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

h = open("historico.csv", "r")
linhas = h.readlines()
historico = []
for i in range (len(linhas)):
    linha = []
    texto = ""
    for j in range (len(linhas[i])):
        if linhas[i][j] != "," and linhas[i][j] != "\n":
            texto += linhas[i][j]
        else:
            linha.append(texto)
            texto = ""
    historico.append(linha)
h.close()

def cadastrar_paciente (clinica, nome, idade, sintoma):
    novo_paciente = [clinica, nome, idade, sintoma]
    cadastros.append(novo_paciente)
    
    arquivo = open("cadastros.csv", "a")
    arquivo.write(clinica + "," + nome + "," + str(idade) + "," + sintoma + "\n")
    arquivo.close()
    return "Paciente cadastrado!"

def cadastrar_paciente_historico (clinica, nome, idade, sintoma):
    novo_paciente = [clinica, nome, idade, sintoma]
    historico.append(novo_paciente)
    
    h = open("historico.csv", "a")
    h.write(clinica + "," + nome + "," + str(idade) + "," + sintoma + "\n")
    h.close()
    return "Paciente cadastrado!"

def exibir_pacientes():
    return cadastros

def remover_paciente(nome,clinica,idade,sintoma):
    encontrado = False
    for k in range(len(cadastros)):
        if cadastros[k][1].lower() == nome.lower() and cadastros[k][0].lower() == clinica.lower():
            encontrado = True 
            del cadastros[k]
            break
    if encontrado == True:
        arquivo = open("cadastros.csv", "w")
        for o in range (len(cadastros)):
            arquivo.write(cadastros[o][0] + "," + cadastros[o][1] + "," + str(cadastros[o][2]) + "," + cadastros[o][3] +"\n")
        arquivo.close()

        h = open("historico.csv", "a")
        h.write(clinica + "," + nome + "," + str(idade) + "," + sintoma + "\n")
        h.close() 

        return "Paciente removido da lista de cadastros."
    else: 
        return "Paciente não encontrado."
    
def remover_paciente_historico(nome,clinica):
    encontrado = False
    for k in range(len(historico)):
        if historico[k][1].lower() == nome.lower() and historico[k][0].lower() == clinica.lower():
            encontrado = True 
            del historico[k]
            break
    if encontrado == True:
        h = open("historico.csv", "w")
        for o in range (len(historico)):
            h.write(historico[o][0] + "," + historico[o][1] + "," + str(historico[o][2]) + "," + historico[o][3] +"\n")
        h.close()
        return "Paciente removido da lista de cadastros."
    else: 
        return "Paciente não encontrado."
    
def buscar_paciente_nome(clinica,nome):
    encontrado = False
    for l in range(len(cadastros)):
        if cadastros[l][1].lower() == nome.lower() and cadastros[l][0].lower() == clinica.lower() :
            encontrado = True 
            return cadastros[l] 
    if encontrado == False: 
        return "Paciente não encontrado."

def buscar_pacientes_sintoma(sintoma,clinica):
    encontrados = []
    for g in range(len(cadastros)):
        if cadastros[g][3].lower() == sintoma.lower() and cadastros[g][0].lower() == clinica.lower() :
            encontrados.append(cadastros[g])
    if len(encontrados) > 0:
        return encontrados
    else:
        return "Paciente não encontrado."

def buscar_pacientes_clinica(clinica):
    encontrados = []
    for z in range(len(cadastros)):
        if cadastros[z][0].lower() == clinica.lower() :
            encontrados.append(cadastros[z])
    if len(encontrados) > 0:
        return encontrados
    else:
        return "Não há pacientes cadastrados nesta clínica."

def alterar_sintoma(nome,novo_sintoma,clinica,idade,sintoma):
    encontrado = False 
    for y in range(len(cadastros)):
        if cadastros[y][1].lower() == nome.lower() and cadastros[y][0].lower() == clinica.lower():
            encontrado = True 
            cadastros[y][3] = novo_sintoma

    if encontrado == True:

        arquivo = open("cadastros.csv", "w")
        
        for o in range (len(cadastros)):
            arquivo.write(cadastros[o][0] + "," + cadastros[o][1] + "," + str(cadastros[o][2]) + "," + cadastros[o][3] +"\n")
        arquivo.close()
        
        
        h = open("historico.csv", "a")
        h.write(clinica + "," + nome + "," + str(idade) + "," + sintoma + "\n")
        h.close()
        
        return "Sintoma alterado."
    else:
        return "Paciente não encontrado."
    
def transferir_paciente(nome,nova_clinica,clinica,idade,sintoma):
    encontrado = False 
    for y in range(len(cadastros)):
        if cadastros[y][1].lower() == nome.lower() and cadastros[y][0].lower() == clinica.lower():
            encontrado = True
            
            cadastros[y][0] = nova_clinica
    if encontrado == True:
        arquivo = open("cadastros.csv", "w")
        
        for o in range (len(cadastros)):
            arquivo.write(cadastros[o][0] + "," + cadastros[o][1] + "," + str(cadastros[o][2]) + "," + cadastros[o][3] +"\n")
        arquivo.close()
        
        h = open("historico.csv", "a")
        h.write(clinica + "," + nome + "," + str(idade) + "," + sintoma + "\n")
        h.close() 
        return "paciente transferido."
    else:
        return "Paciente não encontrado."

def exibir_historico():
    return historico

