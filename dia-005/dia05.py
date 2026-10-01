nome = input("Nome do Cliente:").capitalize()
quant_produto = 0
produtos = []
total_compra = 0
preco_unit = 0 
quant_comprada = 0
tot_item_comprado = 0
while quant_produto <= 0:
    quant_produto =int(input("Quantidade de produtos diferentes:"))
    if quant_produto <= 0:
        print("A quantidade de produtos deve ser maior que Zero")

for i in range(quant_produto):
    produtos.append(input(f"Digite o produto {i+1}:").capitalize())
    while preco_unit <=0:
        preco_unit = float(input("Preço Unitário:"))
        if preco_unit <= 0:
            print("O preço unitário do item deve ser maior que Zero")    
    while quant_comprada <= 0:
        quant_comprada = int(input("Quantidade comprada: "))
        if quant_comprada <= 0:
            print("A quantidade de produtos comprados deve ser maior que Zero")
    total_compra += (preco_unit * quant_comprada)
    tot_item_comprado += quant_comprada
    preco_unit = 0
    quant_comprada = 0
descont = 0
if total_compra >= 500:
    descont = 0.15
elif total_compra >= 300:
    descont = 0.1
elif total_compra >= 100:
    descont = 0.05


valor_desc = total_compra * descont
forma_pagamento = 0
while forma_pagamento not in (1,2,3):
    forma_pagamento = int(input("1 — Dinheiro | 2 — Cartão | 3 — Pix |  "))
    if forma_pagamento not in (1,2,3):
        print("Digite uma forma de pagamento valida!")

print("===== RESUMO DA COMPRA =====")
print(f"Cliente: {nome}")
print(f"Quantidade de produtos diferentes: {quant_produto}")
print(f"Total de unidades:{tot_item_comprado}")
print(f"Subtotal: R${total_compra:.2f}")
print(f"Desconto aplicado: {descont * 100}%")
print(f"Valor do desconto: R${valor_desc:.2f}")
print(f"Valor final R${(total_compra - valor_desc):.2f}")
if forma_pagamento == 1:
    print("Pagamento em Dinheiro.")
elif forma_pagamento == 2:
    print("Pagamento no Cartão.")
else:
    print("Pagamento no Pix")
