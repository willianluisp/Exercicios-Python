print("Bem vindo à tabuada da sua escolha !!")

num = int(input("\nDigite um número para ver a tabuada: "))
print(f"\nTabuada do {num}:")
for i in range(0, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")

opcao = input("\nDeseja ver outra tabuada? (s/n): ")
while opcao.lower() == 's':
    num = int(input("\nDigite um número para ver a tabuada: "))
    print(f"\nTabuada do {num}:")
    for i in range(1, 10):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")
    opcao = input("\nDeseja ver outra tabuada? (s/n): ")
print("Fechando o programa...")

