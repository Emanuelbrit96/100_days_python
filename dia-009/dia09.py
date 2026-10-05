produtos = []
precos = []
quant_produtos = 0

while quant_produtos <= 0:
    quant_produtos = int(
        input("Digite a quantidade de produtos que serão cadastrados: ")
        )
    if quant_produtos <= 0:
        print("A quantidade deve ser maior que zero.")
      
for i in range(quant_produtos):
    print(f"Produto {i+1} de {quant_produtos}: ")
    produto = input("Nome: ").strip().capitalize()
    preco = 0

    while not produto:
                    print(f"Produto {i+1} de {quant_produtos}: ")
                    print("O nome do produto não pode estar vazio!")
                    produto = input("Nome: ").strip().capitalize()

    while preco <= 0:
        entrada_preco = input("Preço: ").strip()
        if not entrada_preco:
            print("O preço não pode estar vazio.")
            continue

        preco = float(entrada_preco)

        if preco <= 0:
            print("O preço deve ser maior que zero.")


    # if not preco:
    #     while not preco:
    #             print("O valor do produto não pode estar vazio!")
    #             preco = float(input("Preço: "))
    #             print(preco)
    #             print(type(preco))        
    # else:
    #     preco = float(preco)    
    #     while preco <= 0:
    #         print("O valor do produto não ser menor ou igual a 0!")
    #         preco = float(input("Preço: "))
    #         print(preco)
    #         print(type(preco))      
   
    produtos.append(produto)
    precos.append(preco)

total_precos = sum(precos)
maior_preco = max(precos)
menor_preco = min(precos)
quant_maior_dez = 0



print("===== PRODUTOS CADASTRADOS =====")
for i in range(quant_produtos):
    print(f"{i+1}. {produtos[i]} - R${precos[i]:.2f}")
    # total_precos += precos[i]
    # if maior_preco < precos[i]:
    #     maior_preco = precos[i]
    # if menor_preco > precos[i]:
    #     menor_preco = precos[i]
    if precos[i] >= 10:
        quant_maior_dez+=1
    

print("===== ANÁLISE =====")
print(f"Quantidade de produtos: {quant_produtos}")
print(f"Soma dos preços: R${total_precos:.2f}")
print(f"Preço médio: R${(total_precos/quant_produtos):.2f}")
print(f"Produto mais caro: {produtos[precos.index(maior_preco)]} - R${maior_preco:.2f}")
print(f"Produto mais barato: {produtos[precos.index(menor_preco)]} - R${menor_preco:.2f}")
print(f"Produtos com preço igual ou superior a R$10.00: {quant_maior_dez}")
