# 1. Pede o texto ao usuário
texto = input("Digite um texto: ")

palavras = texto.split()  
# .split() cria uma lista de palavras, separando onde tem espaço

quantidade_palavras = len(palavras)  
# len() dá o tamanho da lista, ou seja, o número de palavras

# Contando quantas letras existem no texto (sem contar espaços e pontuação)
# Para isso, vamos percorrer o texto e contar só os caracteres que são letras
letras = 0
for letra in texto:
    if letra.isalpha():  # isalpha() verifica se o caractere é uma letra (a-z, A-Z)
        letras += 1     # conta só as letras, ignorando espaços e símbolos

# Identifica a palavra mais longa
palavra_mais_longa = ""
for palavra in palavras:
    if len(palavra) > len(palavra_mais_longa):
        palavra_mais_longa = palavra

# 6. Mostra os resultados para o usuário
print(f"\nQuantidade de palavras: {quantidade_palavras}")
print(f"Quantidade de letras (sem espaços e símbolos): {letras}")
print(f"Palavra mais longa: {palavra_mais_longa}")
