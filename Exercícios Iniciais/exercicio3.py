import string   # fornece letras, números e símbolos
import random   # gera valores aleatórios

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation
""" string.ascii_letters → contém letras maiúsculas e minúsculas (A-Z, a-z)
     string.digits → contém os números (0-9)
     string.punctuation → contém símbolos (!@#$%^&* etc.)
"""
senha = ''.join(random.choice(caracteres) for i in range(tamanho))

"""
Vamos entender essa linha:

random.choice(caracteres) → escolhe 1 caractere aleatório da lista caracteres

for i in range(tamanho) → repete isso o número de vezes que o usuário escolheu

''.join(...) → junta todos os caracteres escolhidos em uma única string (sem espaços)

"""
print(f"Sua senha gerada é: {senha}")