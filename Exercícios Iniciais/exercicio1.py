print("Bem vindo a Calculadora!")

num1 = int(input("\nDigite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

print("\nEscolha a operação que deseja realizar:")
print("\n1: Adição (+)\n2: Subtração (-)\n3: Multiplicação (*)\n4: Divisão (/)")
operacao = input("Digite on número da operação que deseja realizar: ")

if operacao == '1':
    resultado = num1 + num2
    print(f"O resultado da adição é: {resultado}")
elif operacao == '2':
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '4':
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")
else:
    print("Operação inválida. Por favor, escolha uma operação válida.")