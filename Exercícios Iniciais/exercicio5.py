despesas = []  # lista que vai armazenar todas as despesas

while True:
    descricao = input("Digite a descrição da despesa (ou 'sair' para finalizar): ")
    if descricao.lower() == "sair":
        break  # sai do loop se o usuário digitar 'sair'

    valor = float(input("Digite o valor da despesa: R$ "))  # converte para número decimal

    # adiciona a despesa na lista como um dicionário
    despesas.append({"descricao": descricao, "valor": valor})
"""
input() lê o que o usuário digitou.

float() transforma o texto em número com casas decimais.

Cada despesa é adicionada à lista usando append().

"""

if despesas:  # só faz os cálculos se houver despesas registradas
    total = sum(d["valor"] for d in despesas)  # soma todos os valores
    maior = max(d["valor"] for d in despesas)  # maior valor
    menor = min(d["valor"] for d in despesas)  # menor valor
    quantidade = len(despesas)                 # número de despesas

    print("\nResumo das despesas:")
    print(f"Total gasto: R$ {total:.2f}")
    print(f"Número de despesas: {quantidade}")
    print(f"Maior despesa: R$ {maior:.2f}")
    print(f"Menor despesa: R$ {menor:.2f}")
else:
    print("Nenhuma despesa registrada.")

"""
sum() soma os valores.

max() e min() encontram, respectivamente, o maior e o menor valor.

len() retorna o número de despesas.

:.2f formata o valor para 2 casas decimais.

"""