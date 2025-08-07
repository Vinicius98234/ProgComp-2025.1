# Código feito por Vinicius Gabriel de Souza Praxedes e Pedro Henrique Brandão
import funcoesq1


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
        funcoesq1.cadastrarcpf()
    
    elif opcao == 'b':
        funcoesq1.cadastrarmac()
    
    elif opcao == 'c':
        funcoesq1.removermac()
    
    elif opcao == 'd':
        funcoesq1.removercpf()
    
    elif opcao == 'e':
        funcoesq1.listarcpf()
    
    elif opcao == 'f':
        funcoesq1.listarmacs()
    
    elif opcao == 'g':
        funcoesq1.salvarbd()
    
    elif opcao == 'h':
        funcoesq1.lerbd()
    
    elif opcao == 'i':
        print("Saindo do programa...")
        break
    
    else:
        print("Opção inválida! Tente novamente.")
