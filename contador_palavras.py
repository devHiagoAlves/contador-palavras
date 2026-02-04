# criar um contador de palavras
# ele deve ler um arquivo e contar quantas vezes a palavra foi mencionada no arquivo

# 1 abrir e ler o conteudo do arquivo
# 2 dividir o texto em palavras
# 3 contar quantas vezes cada palavra aparece
# 4 mostrar resultado

# 1 abrir o arquivo

conteudo = "Python é incrível. Python é poderoso. Aprender Python é divertido."

# 2 dividir o texto em palavras
palavras = conteudo.split()

# 3 criar um dicionario para contar
contagem = {}
    
for palavra in palavras:
    if palavra in contagem:
        contagem[palavra] += 1
    else:
        contagem[palavra] = 1 
        
#mostrar o resultado
print("Contagem de palavras:\n")
 
for palavra, qtd in contagem.items():
     print(f"{palavra}: {qtd}")
