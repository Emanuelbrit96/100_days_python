perguntas = [
    "Qual função é usada para receber dados do usuário?",
    "Qual estrutura é utilizada para repetição?",
    "Qual método adiciona um elemento ao final de uma lista?",
    "Qual função retorna a quantidade de elementos?",
    "Qual operador verifica se um valor pertence a uma coleção?"
]

alternativas = [
    "A) print() | B) input() | C) len()",
    "A) if | B) while | C) input",
    "A) append() | B) split() | C) strip()",
    "A) sum() | B) max() | C) len()",
    "A) in | B) is | C) and"
]
respostas_corretas = ["B", "B", "A", "C", "A"]
quant_perguntas = len(perguntas)
acertos = 0
respostas = []


start = 0
while start not in (1,2):
    start = int(input("1 — Iniciar o quiz\n" \
    "2 — Sair \n"))
else:
    if start == 1:
        nome = ""

        while not nome:
            nome = input("Digite seu nome:").strip().title()
            if not nome:
                print("O nome não pode estar vazio.")


        for i in range(len(perguntas)):
            print(f'===== QUESTÃO {i+1} DE {quant_perguntas} =====')
            print(perguntas[i])
            print(alternativas[i])
            resposta = input("Resposta:").strip().upper()

            while resposta not in ("A","B","C"):
                print("Alternativa inválida!")
                print(f'===== QUESTÃO {i+1} DE {quant_perguntas} =====')
                print(perguntas[i])
                print(alternativas[i])
                resposta = input("Resposta:").strip().upper()


            if resposta == respostas_corretas[i]:
                acertos += 1
                print("Resposta correta!")
            else:
                print(f"Resposta incorreta! A alternativa correta era a {respostas_corretas[i]}")


            respostas.append(resposta)

        porcentagem_acertos = (acertos/quant_perguntas) * 100
        print(f"Jogador: {nome}")
        print(f"Quantidade de perguntas: {quant_perguntas}")
        print(f"Acertos: {acertos}")
        print(f"Aproveitamento: {porcentagem_acertos:.2f}%")
        print(f"Erros: {quant_perguntas - acertos}%")
        if porcentagem_acertos >= 90:
            print("Classificação: Excelente")
        elif porcentagem_acertos >=70:
            print("Classificação: Muito bom")
        elif porcentagem_acertos >= 40:
            print("Classificação: Razoável")
        else:
            print("Classificação: Precisa revisar")

        print("===== REVISÃO =====")
        for i in range(len(perguntas)): 
            print(f"\nQuestão {i+1}")
            print(f"Sua resposta: {respostas[i]}")
            print(f"Resposta correta: {respostas_corretas[i]}")
            if respostas[i] == respostas_corretas[i]:
                print("Situação: Acertou")
            else:
                print("Situação: Errou")

    else:
        print("Fim do Quiz!")





    