import re
import json
banco_de_dados = {}

def validar_cpf (cpf : str):
    if type(cpf) != str:
        return False
    cpf = cpf.replace(".", "").replace("-", "")
    if cpf.isdecimal() == False:
        return False
    if len(cpf) != 11:
        return False
    
    soma = 0
    for pos in range (9):
        soma += int(cpf[pos]) * (10 - pos)
    dv1 = 11 - soma % 11
    if dv1 >= 10: dv1 = 0
        
    if dv1 != int(cpf[9]):
        return False
    
    soma = 0
    for pos in range (10):
        soma += int(cpf[pos]) * (11 - pos)
    dv2 = 11 - soma % 11
    if dv2 >= 10: dv2 = 0
        
    if dv2 != int(cpf[10]):
        return False
    
    return True

# Validação de MAC address
def validar_mac(mac): 
    padrao = re.compile(r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$')
    return bool(padrao.match(mac))

def cadastrarcpf():
    cpf = input("Digite o CPF (formato: 123.456.789-09 ou 12345678909): ")
    if validar_cpf(cpf): # Se validar o cpf roda o resto 
        if cpf not in banco_de_dados: # Evita duplicatas
            banco_de_dados[cpf] = []
            print("CPF cadastrado com sucesso!")
        else:
            print("Este CPF já está cadastrado!")
    else:
            print("CPF inválido!")

def cadastrarmac():
    cpf = input("Digite o CPF: ")
    if validar_cpf(cpf): 
        if cpf in banco_de_dados: # vê se o cpf está dentro do bd
            mac = input("Digite o MAC address (formato: 00:1A:2B:3C:4D:5E ou 00-1A-2B-3C-4D-5E): ")
            if validar_mac(mac): # Valida o MAC
                if mac not in banco_de_dados[cpf]:
                    banco_de_dados[cpf].append(mac) # Bota o mac em uma lista dentro do cpf
                    print("MAC address adicionado com sucesso!")
                else:
                    print("Este MAC address já está vinculado a este CPF!")
            else:
                print("MAC address inválido!")
        else:
            print("CPF não encontrado no banco de dados!")
    else:
        print("CPF inválido!")

def removermac():
    cpf = input("Digite o CPF: ")
    if validar_cpf(cpf):
        if cpf in banco_de_dados:
            if banco_de_dados[cpf]:
                print("MAC addresses vinculados a este CPF:")
                for i, mac in enumerate(banco_de_dados[cpf], 1): # Enumera os mac em 1 2 e 3 para facilitar e remoção
                    print(f"{i}. {mac}") # Exibe o numero e o mac 
                try:
                    indice = int(input("Digite o número do MAC address a ser removido: ")) - 1 
                    if 0 <= indice < len(banco_de_dados[cpf]): # Se o numero estiver dentro da quantidade de macs remove
                        mac_removido = banco_de_dados[cpf].pop(indice) # Esse pop remove e a lista é atualizada automaticamente
                        print(f"MAC address {mac_removido} removido com sucesso!")
                    else: # SE não da numero invalido 
                        print("Número inválido!")
                except ValueError:
                    print("Entrada inválida! Digite um número.")
            else:
                print("Não há MAC addresses vinculados a este CPF!")
        else:
            print("CPF não encontrado no banco de dados!")
    else:
        print("CPF inválido!")

def removercpf():
    cpf = input("Digite o CPF a ser removido: ")
    if validar_cpf(cpf):
        if cpf in banco_de_dados:
            if not banco_de_dados[cpf]: # Se ele estiver vazio ele remove 
                del banco_de_dados[cpf] # Remove o cpf
                print("CPF removido com sucesso!")
            else: # se não mostra essa mensagem
                print("Não é possível remover o CPF pois existem MAC addresses vinculados a ele!")
        else:
            print("CPF não encontrado no banco de dados!")
    else:
        print("CPF inválido!")

def listarcpf():
    if banco_de_dados:
        print("CPFs cadastrados:")
        for cpf in banco_de_dados:
            print(f"- {cpf}") # Lista os cpf
    else:
        print("Nenhum CPF cadastrado no banco de dados!")

def listarmacs():
    cpf = input("Digite o CPF: ")
    if validar_cpf(cpf):
        if cpf in banco_de_dados:
            if banco_de_dados[cpf]:
                print(f"MAC addresses vinculados ao CPF {cpf}:")
                for mac in banco_de_dados[cpf]:
                    print(f"- {mac}") # Lista os mac vinculados a um cpf
            else:
                print("Nenhum MAC address vinculado a este CPF!")
        else:
            print("CPF não encontrado no banco de dados!")
    else:
        print("CPF inválido!")

def salvarbd():
    if banco_de_dados:
        nome_arquivo = input("Digite o nome do arquivo JSON para salvar (ex: dados.json): ") # Pede ao usuário o nome do arquivo onde os dados serão salvos (ex: dados.json)
        try:
            with open(nome_arquivo, 'w') as arquivo: # Abre o arquivo em modo escrita ('w')
                json.dump(banco_de_dados, arquivo, indent=4) # Salva o dicionário banco_de_dados no arquivo JSON
            print("Banco de dados salvo com sucesso no formato JSON!")
        
        except Exception as e:
            print(f"Erro inesperado: {e}")
    else:
        print("Nenhum dado para salvar!")

def lerbd():
    nome_arquivo = input("Digite o nome do arquivo JSON para ler (ex: dados.json): ")
    try:
        with open(nome_arquivo, 'r') as arquivo: # Abre o arquivo em modo leitura ('r').
            banco_de_dados = json.load(arquivo) # Carrega o conteúdo do arquivo JSON para a variável banco_de_dados.
            # Validar os dados carregados
            dados_validos = True
            for cpf, macs in banco_de_dados.items(): # Percorre cada CPF e sua lista de MACs no dicionário carregado.
                if not validar_cpf(cpf):
                    print(f"CPF inválido encontrado no arquivo: {cpf}")
                    dados_validos = False
                    break
                for mac in macs:
                    if not validar_mac(mac):
                        print(f"MAC address inválido encontrado no arquivo: {mac}")
                        dados_validos = False
                        break
            
            if dados_validos:
                print("Banco de dados carregado com sucesso do arquivo JSON!")
            else:
                banco_de_dados = {} # Se houver dados invalidos reseta o bd
                print("Arquivo contém dados inválidos. Banco de dados não foi carregado.")
    except FileNotFoundError: # Se o arquivo não existir, exibe esta mensagem.
        print("Arquivo não encontrado!")
    except Exception as e:
        print(f"Erro inesperado ao ler o arquivo: {e}")
        banco_de_dados = {}
