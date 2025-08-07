# Código feito por Vinicius Gabriel de Souza Praxedes e Pedro Henrique Brandão

import random

# Cores
VERDE = '\033[1;30;32m'   # Posição correta
AMARELO = '\033[1;30;33m' # Letra existe mas posição errada
CINZA = '\033[1;30;37m'   # Letra não existe
RESET = '\033[0m'         # Resetar cor

print("DUETO\n")

palavras = (
    "ADAGA", "ADUBO", "AMIGO", "ANEXO", "ARAME", "ARARA", "ARROZ",
    "ASILO", "ASTRO", "BAILE", "BAIXA", "BALAO", "BALSA", "BARCO",
    "BARRO", "BEIJO", "BICHO", "BORDA", "BORRA", "BRAVO", "BREJO",
    "BURRO", "CAIXA", "CALDO", "CANJA", "CARRO", "CARTA", "CERVO",
    "CESTA", "CLIMA", "COBRA", "COLAR", "COQUE", "COURO", "CRAVO",
    "DARDO", "FAIXA", "FARDO", "FENDA", "FERRO", "FESTA", "FLUOR",
    "FORCA", "FORNO", "FORTE", "FUNDO", "GAITA", "GARRA", "GENIO",
    "GESSO", "GRADE", "GRANA", "GRAMA", "GURIA", "GREVE", "GRUTA",
    "HEROI", "HOTEL", "ICONE", "IMPAR", "IMUNE", "INDIO", "JUNTA",
    "LAPIS", "LARVA", "LAZER", "LENTO", "LESTE", "LIMPO", "LIVRO",
    "MACIO", "MAGRO", "MALHA", "MANSO", "MARCO", "METAL", "MORTE",
    "MORRO", "MURAL", "MOVEL", "NACAO", "NINHO", "NOBRE", "NORMA",
    "NORTE", "NUVEM", "PACTO", "PALHA", "PARDO", "PARTE", "PEDRA",
    "PEDAL", "PEIXE", "PRADO", "PISTA", "POMBO", "POETA", "PONTO",
    "PRATO", "PRECO", "PRESO", "PROSA", "PRUMO", "PULGA", "PULSO",
    "QUEPE", "RAIVA", "RISCO", "RITMO", "ROSTO", "ROUPA", "SABAO",
    "SALTO", "SENSO", "SINAL", "SITIO", "SONHO", "SOPRO", "SURDO",
    "TARDE", "TERNO", "TERMO", "TERRA", "TIGRE", "TINTA", "TOLDO",
    "TORRE", "TRAJE", "TREVO", "TROCO", "TRONO", "TURMA", "URUBU",
    "VALSA", "VENTO", "VERDE", "VISAO", "VINHO", "VIUVO", "ZEBRA"
) # Palavras Aleatórias

# Selecionar palavras secretas
palavra1 = random.choice(palavras)
palavra2 = random.choice(palavras)

while palavra1 == palavra2: # Não deixa sortear palavras iguais!
    palavra2 = random.choice(palavras)

tentativas = 0 # Tentativas começa 0
acertou_palavra1 = False # Aqui já começa definindo que não acertou a palavras
acertou_palavra2 = False
letras_fora1 = [] # Aqui é para botar as letras que não tem na palavra 1 e 2
letras_fora2 = []

while tentativas < 7 and not (acertou_palavra1 and acertou_palavra2): # Enquanto as tentativas forem menores que 7 e não tiver acertado as palavras continua rodando
    try:
        tentativa = input(f"Tentativa {tentativas+1}/7: ").upper().strip() # Aqui é a tentativa
        
        # Validações dentro do while conforme pedido
        if not tentativa.isalpha():
            raise ValueError("Erro: Digite apenas letras, não use números!")
        if len(tentativa) != 5: # Se a tentativa tiver menos ou mais de 5 letras n roda
            raise ValueError("Palavra deve ter exatamente 5 letras!")
        if tentativa not in palavras: # Se a tentantiva estiver fora do grupo de palavras a tentativa não é aceita
            raise ValueError("Essa palavra não é aceita no jogo!")
        
        # Preparar visualização para cada palavra secreta usando listas
        resultado1 = []
        resultado2 = []
        
        for i in range(5):  # Percorre todas as letras da tentativa
            letra = tentativa[i]
            
            # Se já acertou a palavra 1, mostra tudo verde
            if acertou_palavra1:
                resultado1.append(f"{VERDE}{palavra1[i]}{RESET}")
            else:
                # Verificação normal para palavra1
                if letra == palavra1[i]:
                    resultado1.append(f"{VERDE}{letra}{RESET}")
                elif letra in palavra1:
                    resultado1.append(f"{AMARELO}{letra}{RESET}")
                else:
                    resultado1.append(f"{CINZA}{letra}{RESET}")
                    if letra not in letras_fora1:
                        letras_fora1.append(letra)
            
            # Se já acertou a palavra 2, mostra tudo verde
            if acertou_palavra2:
                resultado2.append(f"{VERDE}{palavra2[i]}{RESET}")
            else:
                # Verificação normal para palavra2
                if letra == palavra2[i]:
                    resultado2.append(f"{VERDE}{letra}{RESET}")
                elif letra in palavra2:
                    resultado2.append(f"{AMARELO}{letra}{RESET}")
                else:
                    resultado2.append(f"{CINZA}{letra}{RESET}")
                    if letra not in letras_fora2:
                        letras_fora2.append(letra)
        
        # Exibe as duas palavras lado a lado parecido com o jogo termo 
        print('\n' + ' '.join(tentativa))
        print(' '.join(resultado1), '   ', ' '.join(resultado2))
        
        # Mostrar letras que não estão em cada palavra (apenas para as não acertadas)
        if not acertou_palavra1 and letras_fora1:
            print(f"Letras fora da 1ª: {' '.join(sorted(letras_fora1))}")
        if not acertou_palavra2 and letras_fora2:
            print(f"Letras fora da 2ª: {' '.join(sorted(letras_fora2))}")
        
        # Verifica se acertou alguma das palavras
        if not acertou_palavra1 and tentativa == palavra1:
            acertou_palavra1 = True
            print(f"\n✅ Acertou a 1ª palavra: {palavra1}")
        if not acertou_palavra2 and tentativa == palavra2:
            acertou_palavra2 = True
            print(f"\n✅ Acertou a 2ª palavra: {palavra2}")
        # Acertou as duas palavras
        if acertou_palavra1 and acertou_palavra2:
            print("\nParabéns! Você acertou ambas as palavras!")
            if tentativas == 0:
                print("Impossível! Você é um gênio!")
            elif tentativas == 1:
                print("Você acertou na segunda tentativa, ninja!")
            elif tentativas == 2:
                print("Você acertou na terceira tentativa, impressionante!")
            elif tentativas == 3:
                print("Você acertou na quarta tentativa, interessante!")
            elif tentativas == 4:
                print("Você acertou na quinta tentativa, pode melhorar!")
            elif tentativas == 5:
                print("Você acertou na sexta tentativa, foi por pouco!")
            break
        
        tentativas += 1 # Conta tentativa

    except ValueError as e: # Trata os erros de valor
        print(e)
        continue
    except Exception as e: # Trata outro tipo de erro
        print(f"Erro inesperado: {e}")
        continue

if not (acertou_palavra1 and acertou_palavra2): # Se acabar o numero de tentativas e n acertar nenhuma das palavras ai acaba o jogo
    print(f"\nFim de jogo! As palavras eram: {palavra1} e {palavra2}")