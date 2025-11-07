import time

print("\n----------Contagem Regressiva----------")
tempo = int(input("Digite o tempo em segundos para contagem regressiva: "))

while tempo > 0:
    print(f"Tempo restante: {tempo} segundos", end="\r")  # o end="\r" faz o texto atualizar na mesma linha
    time.sleep(1)  # espera 1 segundo
    tempo -= 1
print("Tempo esgotado!")