frase = input("Digite uma frase:").strip()
while not frase:
    print("A frase não pode estar vazia.")
    frase = input("Digite uma frase:").strip()

espaco = 0
tamanho_frase = len(frase)
vogais = 0
palavras = frase.split()
numero = 0
caracter_espec = 0
consoante = 0


for letra in frase:
    if letra.isspace():
        espaco += 1
    elif letra.lower() in "aeiouáàâãéêíóôõú":
        vogais += 1
    elif letra.isalpha():
        consoante += 1
    elif letra.isdigit():
        numero += 1
    else:
        caracter_espec += 1





print("===== ANÁLISE DO TEXTO =====")
print(f"Texto: {frase}")
print(f"Total de caracteres: {tamanho_frase}")
print(f"Caracteres sem espaços: {tamanho_frase - espaco}")
print(f"Quantidade de palavras: {len(palavras)}")
print(f"Vogais: {vogais}")
print(f"Consoantes: {consoante}")
print(f"Números: {numero}")
print(f"Espaços: {espaco}")
print(f"Caracteres especiais: {caracter_espec}")