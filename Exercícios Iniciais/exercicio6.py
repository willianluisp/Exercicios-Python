print("Bem vindo ao programa de cadastro !!")

usuarios = []  # lista para armazenar os dados dos usuários

# Primeiro cadastro obrigatório
nome = input("\nDigite o nome: ")
idade = int(input("Digite a idade: "))
email = input("Digite o email: ")

usuarios.append({"nome": nome,
                 "idade": idade,
                 "email": email
                })

while True:
    opcao = input("\nDeseja cadastrar outro usuário? (s/n): ")
    if opcao.lower() == 's':
        nome = input("\nDigite o nome: ")
        idade = int(input("Digite a idade: "))
        email = input("Digite o email: ")

        usuarios.append({"nome": nome,
                         "idade": idade,
                         "email": email
                        })
    else:
        break  # sai do laço se não quiser cadastrar mais

print("\nCadastro finalizado.")
opcao = input("Deseja ver os dados cadastrados? (s/n): ")
if opcao.lower() == 's':
    # Percorre a lista 'usuarios' e mostra os dados de cada pessoa
    # 'i' é o número do usuário (começa em 1)
    # 'usuario' é o dicionário com nome, idade e email
    for i, usuario in enumerate(usuarios, 1):

        # Mostra o número do usuário
        print(f"\nUsuário {i}:")
    
        # Mostra o nome da pessoa (pega da chave 'nome')
        print(f"Nome: {usuario['nome']}")
    
        # Mostra a idade da pessoa (pega da chave 'idade')
        print(f"Idade: {usuario['idade']}")
    
        # Mostra o email da pessoa (pega da chave 'email')
        print(f"Email: {usuario['email']}")
        opcao = input("\nDeseja sair do programa? (s/n): ")
        if opcao.lower() == 's':
            print("Saindo do programa.")
        else:
            print("\nSaindo do mesmo jeito..")

else:
    opcao = input("Deseja sair do programa? (s/n): ")
    if opcao.lower() == 's':
        print("Saindo do programa.")
    else:
            print("\nSaindo do mesmo jeito..")
