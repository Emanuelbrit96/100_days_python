name = input("Digite seu nome: ").capitalize()
age = int(input("Digite sua idade: "))

if age < 0:
    print("Valor Invalido.")
elif age < 16:
    print("===== CONTROLE DE ACESSO =====")
    print(f"Nome: {name}")
    print(f"Idade: {age}")
    print(f"Situação: Entrada negada.")  
    print(f"Motivo: Idade abaixo do limite permitido")
else:
    ticket =  input("Possui ingresso? (s/n)").lower()
    if ticket not in ("s","n"):
        print("Dados inválidos.")
    else:
        if ticket == "n":
            print("===== CONTROLE DE ACESSO =====")
            print(f"Nome: {name}")
            print(f"Idade: {age}")
            print(f"Situação: Entrada negada.")  
            print(f"Motivo: Não possui ingresso")
        
        elif age < 18:    
            resp = input("Está acompanhado de um responsável: (s/n)").lower()
            if resp not in ("s","n"):
                print("Dados inválidos.")
            else:
                if resp == "n":
                    print("===== CONTROLE DE ACESSO =====")
                    print(f"Nome: {name}")
                    print(f"Idade: {age}")
                    print(f"Situação: Entrada negada.")  
                    print(f"Motivo: Menor de idade sem responsável")
                else:
                    print("===== CONTROLE DE ACESSO =====")
                    print(f"Nome: {name}")
                    print(f"Idade: {age}")
                    print(f"Situação: Entrada permitida acompanhado do responsável.")
        else:
            print("===== CONTROLE DE ACESSO =====")
            print(f"Nome: {name}")
            print(f"Idade: {age}")
            print(f"Situação: Entrada permitida.") 
