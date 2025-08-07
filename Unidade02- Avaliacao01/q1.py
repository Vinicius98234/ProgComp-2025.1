import json
import funcoesq1
banco_de_dados = {} # Banco de dados 

while True:
    print("\nMenu de Operações:") # Menu para escolher o que fazer
    print("a) Cadastrar CPF")
    print("b) Adicionar MAC address a um CPF")
    print("c) Remover um MAC address de um CPF")
    print("d) Remover o CPF")
    print("e) Listar os CPFs cadastrados")
    print("f) Listar os MAC addresses vinculados a um CPF")
    print("g) Salvar o banco de dados em um arquivo")
    print("h) Ler o banco de dados de um arquivo")
    print("i) Sair")
    
    opcao = input("Escolha uma opção: ").lower() # Escolher a função
    

    if opcao == 'a':
        cpf = input("Digite o CPF (formato: 123.456.789-09 ou 12345678909): ")
        if funcoesq1.validar_cpf(cpf): # Se validar o cpf roda o resto 
            if cpf not in banco_de_dados: # Evita duplicatas
                banco_de_dados[cpf] = []
                print("CPF cadastrado com sucesso!")
            else:
                print("Este CPF já está cadastrado!")
        else:
            print("CPF inválido!")
    
    elif opcao == 'b':
        cpf = input("Digite o CPF: ")
        if funcoesq1.validar_cpf(cpf): 
            if cpf in banco_de_dados: # vê se o cpf está dentro do bd
                mac = input("Digite o MAC address (formato: 00:1A:2B:3C:4D:5E ou 00-1A-2B-3C-4D-5E): ")
                if funcoesq1.validar_mac(mac): # Valida o MAC
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
    
    elif opcao == 'c':
        cpf = input("Digite o CPF: ")
        if funcoesq1.validar_cpf(cpf):
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
    
    elif opcao == 'd':
        cpf = input("Digite o CPF a ser removido: ")
        if funcoesq1.validar_cpf(cpf):
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
    
    elif opcao == 'e':
        if banco_de_dados:
            print("CPFs cadastrados:")
            for cpf in banco_de_dados:
                print(f"- {cpf}") # Lista os cpf
        else:
            print("Nenhum CPF cadastrado no banco de dados!")
    
    elif opcao == 'f':
        cpf = input("Digite o CPF: ")
        if funcoesq1.validar_cpf(cpf):
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
    
    elif opcao == 'g':
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
    
    elif opcao == 'h':
        nome_arquivo = input("Digite o nome do arquivo JSON para ler (ex: dados.json): ")
        try:
            with open(nome_arquivo, 'r') as arquivo: # Abre o arquivo em modo leitura ('r').
                banco_de_dados = json.load(arquivo) # Carrega o conteúdo do arquivo JSON para a variável banco_de_dados.
                # Validar os dados carregados
                dados_validos = True
                for cpf, macs in banco_de_dados.items(): # Percorre cada CPF e sua lista de MACs no dicionário carregado.
                    if not funcoesq1.validar_cpf(cpf):
                        print(f"CPF inválido encontrado no arquivo: {cpf}")
                        dados_validos = False
                        break
                    for mac in macs:
                        if not funcoesq1.validar_mac(mac):
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
    
    elif opcao == 'i':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")