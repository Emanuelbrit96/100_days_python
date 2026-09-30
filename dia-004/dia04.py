nome = input("Digite o nome do estudante:").capitalize()
disciplina = input("Digite a disciplina:").capitalize()
quant_ava =  int(input("Digite a quantidade de avaliações:"))
notas = 0
i=1

if quant_ava <= 0:
    print("A quantidade de avaliações deve ser maior que zero.")
else:
    while i <= quant_ava:
        nota = float(input(f"Digite {i}ª nota: "))
        if nota < 0 or nota > 10:
            print("Nota inválida! Digite um número entre 0 e 10.")
            continue

        notas += nota
        i+=1   
    

    media = notas / quant_ava
    situacao = ""
    if media < 5:
        situacao = "Reprovado"
    elif media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Recuperação"

    print("===== RESULTADO FINAL =====")
    print(f"Estudante: {nome}")
    print(f"Disciplina: {disciplina}")
    print(f"Quantidade de avaliações: {quant_ava}")
    print(f"Soma das notas: {notas:.2f}")
    print(f"Média final: {media:.2f}")
    print(f"Situação: {situacao}")

