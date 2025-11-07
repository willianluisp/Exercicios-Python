print("\n----------Calculador de Médias----------")
alunos = []  # lista para armazenar as notas

# Primeiro aluno
nomeAluno = input("\nDigite o nome do primeiro aluno: ")
nota1 = float(input(f"Digite a primeira nota de {nomeAluno}: "))
nota2 = float(input(f"Digite a segunda nota de {nomeAluno}: "))
media = (nota1 + nota2) / 2
alunos.append({"nome": nomeAluno, "Primeira Nota": nota1, "Segunda Nota": nota2, "media": media})

# Loop para adicionar outros alunos
while True:
    opcao = input("\nDeseja adicionar outro aluno? (s/n): ")
    if opcao.lower() == 's':
        nomeAluno = input("\nDigite o nome do próximo aluno: ")
        nota1 = float(input(f"Digite a primeira nota de {nomeAluno}: "))
        nota2 = float(input(f"Digite a segunda nota de {nomeAluno}: "))
        media = (nota1 + nota2) / 2
        alunos.append({"nome": nomeAluno, "Primeira Nota": nota1, "Segunda Nota": nota2, "media": media})
    else:
        break  # sai do loop se o usuário não quiser adicionar mais alunos

# Mostrar resultados
print("\nCálculo finalizado.")
opcao = input("Deseja ver as médias calculadas? (s/n): ")
if opcao.lower() == 's':
    for i, aluno in enumerate(alunos, 1):
        print(f"\nAluno {i}:")
        print(f"Nome: {aluno['nome']}")
        print(f"Primeira Nota: {aluno['Primeira Nota']}")
        print(f"Segunda Nota: {aluno['Segunda Nota']}")
        print(f"Média: {aluno['media']}")
else:
    print("Fechando o programa...")
