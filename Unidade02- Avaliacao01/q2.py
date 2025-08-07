# Código feito por Vinicius Gabriel de Souza Praxedes e Pedro Henrique Brandão

try:
    count  = 0 # Inicializa o contador de números palíndromos
    for num in range(10,100000+1): # Percorre os números de 10 a 100000
        numfinal = num # Guarda o número original para comparação
        n = 0 # Inicializa a variável para armazenar o número invertido

        while num > 0: # Inverte o número
            algarismo = num % 10
            num = num // 10
            n = 10 * n + algarismo
            
        if n == numfinal: # Verifica se o número invertido é igual ao original
            count += 1
    print("Tem",count, "números palíndromos entre 10 e 100000") # Exibe a quantidade de números palíndromos encontrados
except Exception as e:
    print("Erro:", e) #Em caso de erro, exibe a mensagem de erro