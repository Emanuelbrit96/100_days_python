import random
num = random.randint(1,100)
i=1

nome = input("Digite seu nome: ")
print("===== JOGO DE ADIVINHAÇÃO =====")
print("Adivinhe o número entre 1 e 100.")
print("Você possui 7 tentativas.")


while i <= 7:
    print(f"Tentativa {i} de 7")
    palpite = int(input("Digite seu palpite: "))
    if palpite < 1 or palpite > 100:
        print("Palpite inválido! Digite um número entre 1 e 100.")
        continue
    elif palpite == num:
        print(f"Parabéns, {nome}!")
        print(f"Você acertou o número {num} na {i}ª tentativa.")
        break
    else:
        if palpite > num:
            print("O número secreto é menor.")
        else:
            print("O número secreto é maior.")
        i+=1
else:
    print("Suas tentativas acabaram!")
    print(f"O número secreto era {num}")
