print("Digite o nome do cliente: ")
nome_cliente = input()
print("Digite o nome do produto: ")
nome_produto = input()
print("Digite valor da compra")
valor_compra = float(input())
desconto = 0

if valor_compra > 0:
    if valor_compra >= 500:
        desconto = 15
    elif valor_compra >= 300:
        desconto = 10
    elif valor_compra >= 100:
        desconto = 5
    valor_desconto = valor_compra * (desconto / 100)
    valor_final = valor_compra - valor_desconto

    print(f"Cliente: {nome_cliente}")
    print(f"Produto: {nome_produto}")
    print(f"Valor original: R${valor_compra:.2f}")
    print(f"Desconto aplicado: {desconto}%")
    print(f"Valor do desconto: R${valor_desconto:.2f}")
    print(f"Valor final: R${valor_final:.2f}")    
else:
    print("Valor Incorreto!")


