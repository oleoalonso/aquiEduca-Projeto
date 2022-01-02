from flask import Flask, request
from flask_cors import CORS, cross_origin
import json
import csv
from csv import writer

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


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
# V A L O R
valorFile = '../csv/valores.csv'
# ###############################################
# R E S E R V A
reservaFile = '../csv/reservas.csv'
# ###############################################
# P A C O T E
pacoteFile = '../csv/pacotes.csv'
# ###############################################
# E V E N T O S
eventoFile = '../csv/eventos.csv'
# ###############################################
# D E P O I M E N T O S
depoimentoFile = '../csv/depoimentos.csv'
# ###############################################
# A T E N D I M E N T O
atendimentoFile = '../csv/atendimentos.csv'
# ###############################################





# *******************************************************
# ********************* ACOMODAÇÃO *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/acomodacao/inserir', methods=['POST'])
def inserirAcomodacao():
    acomodacao = json.loads(request.data)
    inserirAcomodacaoCsv(acomodacao)
    return { 'message': 'Acomodação adicionado com sucesso' }  

@app.route('/acomodacao/listar', methods=['GET'])
def listarAcomodacao():
    acomodacoes = listarAcomodacaoCsv()
    return json.dumps(acomodacoes)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/acomodacao/deletar/<nroLinha>', methods=['DELETE'])
def deletarAcomodacao(nroLinha):
    acomodacoes = listarAcomodacaoCsv()
    novosAcomodacoes = []       

    i = 0
    for acomodacao in acomodacoes:        
        if int(nroLinha) != i:
            novosAcomodacoes.append(acomodacao)
        i = i + 1

    reinserirAcomodacaoCsv(novosAcomodacoes)
    return { 'message': 'Acomodação deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarAcomodacaoCsv():
    acomodacoes = []
    with open(acomodacaoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: # aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                acomodacoes.append({ 
                    'nome': linha[0],
                    'tipo': linha[1],                     
                    'qtdCama': linha[2]                 
                })
            count += 1

    return acomodacoes

def inserirAcomodacaoCsv(acomodacao):
    novaLinha = [acomodacao["nome"], acomodacao["tipo"], acomodacao["qtdCama"]]
    with open(acomodacaoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirAcomodacaoCsv(acomodacoes):
    linhas = []
    linhas.append(["nome", "tipo", "qtdCama"]) # é necessário inserir novamente o cabeçalho da planilha

    for acomodacao in acomodacoes:
        novaLinha = [acomodacao["nome"], acomodacao["tipo"], acomodacao["qtdCama"]]
        linhas.append(novaLinha)

    with open(acomodacaoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* ACOMODAÇÃO *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<    





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





# *******************************************************
# ********************* VALORES *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/valor/inserir', methods=['POST'])
def inserirValor():
    valor = json.loads(request.data)
    inserirValorCsv(valor)
    return { 'message': 'Valor adicionado com sucesso' }  

@app.route('/valor/listar', methods=['GET'])
def listarValor():
    valores = listarValorCsv()
    return json.dumps(valores)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/valor/deletar/<nroLinha>', methods=['DELETE'])
def deletarValor(nroLinha):
    valores = listarValorCsv()
    novosValores = []       

    i = 0
    for valor in valores:        
        if int(nroLinha) != i:
            novosValores.append(valor)
        i = i + 1

    reinserirValorCsv(novosValores)
    return { 'message': 'Valor deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarValorCsv():
    valores = []
    with open(valorFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                valores.append({ 
                    'tipo': linha[0],
                    'valor': linha[1]                    
                })
            count += 1

    return valores

def inserirValorCsv(valor):
    novaLinha = [valor["tipo"], valor["valor"]]
    with open(valorFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirValorCsv(valores):
    linhas = []
    linhas.append(["tipo", "valor"]) # é necessário inserir novamente o cabeçalho da planilha

    for valor in valores:
        novaLinha = [valor["tipo"], valor["valor"]]
        linhas.append(novaLinha)

    with open(valorFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* VALOR *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<





# *******************************************************
# ********************* RESERVA *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/reserva/inserir', methods=['POST'])
def inserirReserva():
    reserva = json.loads(request.data)
    inserirReservaCsv(reserva)
    return { 'message': 'Reserva adicionado com sucesso' }  

@app.route('/reserva/listar', methods=['GET'])
def listarReserva():
    reservas = listarReservaCsv()
    return json.dumps(reservas)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/reserva/deletar/<nroLinha>', methods=['DELETE'])
def deletarReserva(nroLinha):
    reservas = listarReservaCsv()
    novosReservas = []       

    i = 0
    for reserva in reservas:        
        if int(nroLinha) != i:
            novosReservas.append(reserva)
        i = i + 1

    reinserirReservaCsv(novosReservas)
    return { 'message': 'Reserva deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarReservaCsv():
    reservas = []
    with open(reservaFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                reservas.append({ 
                    'nome': linha[0],
                    'cpf': linha[1],                     
                    'email': linha[2],
                    'telefone': linha[3],
                    'acomodacao': linha[4],
                    'dataEntrada': linha[5],
                    'dataSaida': linha[6]                                                                                 
                })
            count += 1

    return reservas

def inserirReservaCsv(reserva):
    novaLinha = [reserva["nome"], reserva["cpf"], reserva["email"], reserva["telefone"], reserva["acomodacao"], reserva["dataEntrada"], reserva["dataSaida"]]
    with open(reservaFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirReservaCsv(reservas):
    linhas = []
    linhas.append(["nome", "cpf", "email", "telefone", "acomodacao", "dataEntrada", "dataSaida"]) # é necessário inserir novamente o cabeçalho da planilha

    for reserva in reservas:
        novaLinha = [reserva["nome"], reserva["cpf"], reserva["email"], reserva["telefone"], reserva["acomodacao"], reserva["dataEntrada"], reserva["dataSaida"]]
        linhas.append(novaLinha)

    with open(reservaFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* RESERVA *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<





# *******************************************************
# ********************* PACOTES *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/pacote/inserir', methods=['POST'])
def inserirPacote():
    pacote = json.loads(request.data)
    inserirPacoteCsv(pacote)
    return { 'message': 'Pacote adicionado com sucesso' }  

@app.route('/pacote/listar', methods=['GET'])
def listarPacote():
    pacotes = listarPacoteCsv()
    return json.dumps(pacotes)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/pacote/deletar/<nroLinha>', methods=['DELETE'])
def deletarPacote(nroLinha):
    pacotes = listarPacoteCsv()
    novosPacotes = []       

    i = 0
    for pacote in pacotes:        
        if int(nroLinha) != i:
            novosPacotes.append(pacote)
        i = i + 1

    reinserirPacoteCsv(novosPacotes)
    return { 'message': 'Pacote deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarPacoteCsv():
    pacotes = []
    with open(pacoteFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                pacotes.append({ 
                    'nome': linha[0],
                    'periodo': linha[1],                     
                    'valor': linha[2]                  
                })
            count += 1

    return pacotes

def inserirPacoteCsv(pacote):
    novaLinha = [pacote["nome"], pacote["periodo"], pacote["valor"]]
    with open(pacoteFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirPacoteCsv(pacotes):
    linhas = []
    linhas.append(["nome", "periodo", "valor"]) # é necessário inserir novamente o cabeçalho da planilha

    for pacote in pacotes:
        novaLinha = [pacote["nome"], pacote["periodo"], pacote["valor"]]
        linhas.append(novaLinha)

    with open(pacoteFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* PACOTES *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<





# *******************************************************
# ********************* EVENTOS *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/evento/inserir', methods=['POST'])
def inserirEvento():
    evento = json.loads(request.data)
    inserirEventoCsv(evento)
    return { 'message': 'Evento adicionado com sucesso' }  

@app.route('/evento/listar', methods=['GET'])
def listarEvento():
    eventos = listarEventoCsv()
    return json.dumps(eventos)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/evento/deletar/<nroLinha>', methods=['DELETE'])
def deletarEvento(nroLinha):
    eventos = listarEventoCsv()
    novosEventos = []       

    i = 0
    for evento in eventos:        
        if int(nroLinha) != i:
            novosEventos.append(evento)
        i = i + 1

    reinserirEventoCsv(novosEventos)
    return { 'message': 'Evento deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarEventoCsv():
    eventos = []
    with open(eventoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                eventos.append({ 
                    'nome': linha[0],
                    'data': linha[1],                     
                    'horario': linha[2],
                    'descricao': linha[3]                     
                })
            count += 1

    return eventos

def inserirEventoCsv(evento):
    novaLinha = [evento["nome"], evento["data"], evento["horario"], evento["descricao"]]
    with open(eventoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirEventoCsv(eventos):
    linhas = []
    linhas.append(["nome", "data", "horario", "descricao"]) # é necessário inserir novamente o cabeçalho da planilha

    for evento in eventos:
        novaLinha = [evento["nome"], evento["data"], evento["horario"], evento["descricao"]]
        linhas.append(novaLinha)

    with open(eventoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* EVENTOS *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<





# *******************************************************
# ********************* DEPOIMENTOS *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/depoimento/inserir', methods=['POST'])
def inserirDepoimento():
    depoimento = json.loads(request.data)
    inserirDepoimentoCsv(depoimento)
    return { 'message': 'Depoimento adicionado com sucesso' }  

@app.route('/depoimento/listar', methods=['GET'])
def listarDepoimento():
    depoimentos = listarDepoimentoCsv()
    return json.dumps(depoimentos)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/depoimento/deletar/<nroLinha>', methods=['DELETE'])
def deletarDepoimento(nroLinha):
    depoimentos = listarDepoimentoCsv()
    novosDepoimentos = []       

    i = 0
    for depoimento in depoimentos:        
        if int(nroLinha) != i:
            novosDepoimentos.append(depoimento)
        i = i + 1

    reinserirDepoimentoCsv(novosDepoimentos)
    return { 'message': 'Depoimento deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarDepoimentoCsv():
    depoimentos = []
    with open(depoimentoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                depoimentos.append({ 
                    'nome': linha[0],
                    'depoimento': linha[1]                   
                })
            count += 1

    return depoimentos

def inserirDepoimentoCsv(depoimento):
    novaLinha = [depoimento["nome"], depoimento["depoimento"]]
    with open(depoimentoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirDepoimentoCsv(depoimentos):
    linhas = []
    linhas.append(["nome", "depoimento"]) # é necessário inserir novamente o cabeçalho da planilha

    for depoimento in depoimentos:
        novaLinha = [depoimento["nome"], depoimento["depoimento"]]
        linhas.append(novaLinha)

    with open(depoimentoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* DEPOIMENTOS *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<





# *******************************************************
# ********************* ATENDIMENTOS *********************
# 
# >>>>>>>>  i n i c i o   <<<<<<<<<
# 
# [ a t r i b u t o s ]

@app.route('/atendimento/inserir', methods=['POST'])
def inserirAtendimento():
    atendimento = json.loads(request.data)
    inserirAtendimentoCsv(atendimento)
    return { 'message': 'Atendimento adicionado com sucesso' }  

@app.route('/atendimento/listar', methods=['GET'])
def listarAtendimento():
    atendimentos = listarAtendimentoCsv()
    return json.dumps(atendimentos)    

# para a exclusão, é necessário reconstruir toda a planilha
# pra isso, faremos a obtenção de todos os dados da planilha e adicionaremos todos novamente com exceção
# ao número da linha que virá como parâmetro neste método (end-point)
@app.route('/atendimento/deletar/<nroLinha>', methods=['DELETE'])
def deletarAtendimento(nroLinha):
    atendimentos = listarAtendimentoCsv()
    novosAtendimentos = []       

    i = 0
    for atendimento in atendimentos:        
        if int(nroLinha) != i:
            novosAtendimentos.append(atendimento)
        i = i + 1

    reinserirAtendimentoCsv(novosAtendimentos)
    return { 'message': 'Atendimento deletado com sucesso' }

# *******************************************************
# *******************************************************
# 
# [ C O N S T R U T O R ]

def listarAtendimentoCsv():
    atendimentos = []
    with open(atendimentoFile, 'r', encoding='latin-1') as planilha:
        tabela = csv.reader(planilha, delimiter=';')
        count = 1        
        for linha in tabela:
            if count != 1: #aqui estamos pulando a linha que corresponde ao cabeçalho do csv
                atendimentos.append({ 
                    'nome': linha[0],
                    'email': linha[1],                     
                    'telefone': linha[2],
                    'mensagem': linha[3]                     
                })
            count += 1

    return atendimentos

def inserirAtendimentoCsv(atendimento):
    novaLinha = [atendimento["nome"], atendimento["email"], atendimento["telefone"], atendimento["mensagem"]]
    with open(atendimentoFile, 'a', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerow(novaLinha)  
        planilha.close()

def reinserirAtendimentoCsv(atendimentos):
    linhas = []
    linhas.append(["nome", "email", "telefone", "mensagem"]) # é necessário inserir novamente o cabeçalho da planilha

    for atendimento in atendimentos:
        novaLinha = [atendimento["nome"], atendimento["email"], atendimento["telefone"], atendimento["mensagem"]]
        linhas.append(novaLinha)

    with open(atendimentoFile, 'w', newline='') as planilha:  
        writer_object = writer(planilha, delimiter=';')
        writer_object.writerows(linhas)  
        planilha.close()

# *******************************************************
# ********************* ATENDIMENTOS *********************
# 
# >>>>>>>>  f i m   <<<<<<<<<

