from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import csv
from csv import writer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

clienteFile = '../csv/acomodacoes.csv'
# ###############################################
# A C O M O D A Ç Ã O
acomodacaoFile = '../csv/acomodacoes.csv'
# ###############################################
# F U N C I O N Á R I O
funcionarioFile = '../csv/funcionarios.csv'
# ###############################################
# H Ó S P E D E
hospedeFile = '../csv/hospedes.csv'
# ###############################################

# *******************************************************
@app.route('/cliente/inserir', methods=['POST'])
def inserirCliente():
    cliente = json.loads(request.data)
    inserirClienteCsv(cliente)
    return { 'message': 'Acomodação adicionado com sucesso' }


@app.route('/cliente/listar', methods=['GET'])
def listarCliente():
    clientes = listarClienteCsv()
    return json.dumps(clientes)

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/cliente/deletar/<nroLinha>', methods=['DELETE'])
def deletarCliente(nroLinha):
    clientes = listarClienteCsv()
    novosClientes = []       

    i = 0
    for cliente in clientes:        
        if int(nroLinha) != i:
            novosClientes.append(cliente)
        i = i + 1

    reinserirClienteCsv(novosClientes)
    return { 'message': 'Cliente deletado com sucesso' }







# *******************************************************
# d e f
# 
# F U N Ç Õ E S 

def listarClienteCsv():
    clientes = []
    with open(clienteFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                clientes.append({ 
                    'nome': linha[0], 
                    'telefone': linha[1], 
                    'email': linha[2] 
                })
            count += 1

    return clientes

def inserirClienteCsv(cliente):
    novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"]]
    with open(clienteFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirClienteCsv(clientes):
    linhas = []
    linhas.append(["nome", "telefone", "email"]) #é necessário inserir novamente o cabeçalho da planilha

    for cliente in clientes:
        novaLinha = [cliente["nome"], cliente["telefone"], cliente["email"]]
        linhas.append(novaLinha)

    with open(clienteFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()










# *******************************************************
# ********************* FUNCIONÁRIO *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/funcionario/inserir', methods=['POST'])
def inserirFuncionario():
    funcionario = json.loads(request.data)
    inserirFuncionarioCsv(funcionario)
    return { 'message': 'Funcionário adicionado com sucesso' }  

@app.route('/funcionario/listar', methods=['GET'])
def listarFuncionario():
    funcionarios = listarFuncionarioCsv()
    return json.dumps(funcionarios)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/funcionario/deletar/<nroLinha>', methods=['DELETE'])
def deletarFuncionario(nroLinha):
    funcionarios = listarFuncionarioCsv()
    novosFuncionarios = []       

    i = 0
    for funcionario in funcionarios:        
        if int(nroLinha) != i:
            novosFuncionarios.append(funcionario)
        i = i + 1

    reinserirFuncionarioCsv(novosFuncionarios)
    return { 'message': 'Funcionário deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarFuncionarioCsv():
    funcionarios = []
    with open(funcionarioFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: # aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                funcionarios.append({ 
                    'nome': linha[0],
                    'cpf': linha[1],                     
                    'email': linha[2],
                    'telefone': linha[3]                     
                })
            count += 1

    return funcionarios

def inserirFuncionarioCsv(funcionario):
    novaLinha = [funcionario["nome"], funcionario["cpf"], funcionario["email"], funcionario["telefone"]]
    with open(funcionarioFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirFuncionarioCsv(funcionarios):
    linhas = []
    linhas.append(["nome", "cpf", "email", "telefone"]) # é necessário inserir novamente o cabeçalho da planilha

    for funcionario in funcionarios:
        novaLinha = [funcionario["nome"], funcionario["cpf"], funcionario["email"], funcionario["telefone"]]
        linhas.append(novaLinha)

    with open(funcionarioFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* FUNCIONÁRIO *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<        






# *******************************************************
# ********************* HÓSPEDE *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/hospede/inserir', methods=['POST'])
def inserirHospede():
    hospede = json.loads(request.data)
    inserirHospedeCsv(hospede)
    return { 'message': 'Hóspede adicionado com sucesso' }  

@app.route('/hospede/listar', methods=['GET'])
def listarHospede():
    hospedes = listarHospedeCsv()
    return json.dumps(hospedes)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/hospede/deletar/<nroLinha>', methods=['DELETE'])
def deletarHospede(nroLinha):
    hospedes = listarHospedeCsv()
    novosHospedes = []       

    i = 0
    for hospede in hospedes:        
        if int(nroLinha) != i:
            novosHospedes.append(hospede)
        i = i + 1

    reinserirHospedeCsv(novosHospedes)
    return { 'message': 'Hóspede deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarHospedeCsv():
    hospedes = []
    with open(hospedeFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                hospedes.append({ 
                    'nome': linha[0],
                    'cpf': linha[1],                     
                    'email': linha[2],
                    'telefone': linha[3]                     
                })
            count += 1

    return hospedes

def inserirHospedeCsv(hospede):
    novaLinha = [hospede["nome"], hospede["cpf"], hospede["email"], hospede["telefone"]]
    with open(hospedeFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirHospedeCsv(hospedes):
    linhas = []
    linhas.append(["nome", "cpf", "email", "telefone"]) # é necessário inserir novamente o cabeçalho da planilha

    for hospede in hospedes:
        novaLinha = [hospede["nome"], hospede["cpf"], hospede["email"], hospede["telefone"]]
        linhas.append(novaLinha)

    with open(hospedeFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* HÓSPEDE *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<
