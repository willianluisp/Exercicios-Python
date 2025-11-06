import random 

def jogar_adivinhacao():
    return random.randint(1, 10)
numero_aleatorio = jogar_adivinhacao()

print("\nBem vindo ao jogo de adivinhação!")
print("Tente adivinhar o número aleatório, entre 1 e 10.")
if numero_aleatorio % 2 == 0:
    print("Dica: O número é par.")
else:
    print("Dica: O número é ímpar.")
print("\nVocê tem 3 tentativas para adivinhar o número.")
tentativas = 3

numeroEscolhido = int(input("Tente adivinhar o número: "))
while numeroEscolhido != numero_aleatorio and tentativas > 1:
    tentativas -= 1
    if numeroEscolhido < numero_aleatorio:
        print("O número é maior.")
    else:
        print("O número é menor.")
    print(f"Você tem {tentativas} tentativas restantes.")
    numeroEscolhido = int(input("Tente adivinhar o número: "))
if tentativas == 0 and numeroEscolhido != numero_aleatorio:
    print(f"Suas tentativas acabaram. O número era {numero_aleatorio}.")
else:
    print("Parabéns! Você adivinhou o número corretamente.")