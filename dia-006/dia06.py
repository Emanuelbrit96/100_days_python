nome = input("Digite seu nome:")
senha  = ""
maiusculo = 0
minusculo = 0
numeral = 0
espaco = 0 
caracter_especial = 0

#Loop que valida o minimo de 8 caracteres
while len(senha) < 8:
    senha = input("Digite a senha: ")
    if len(senha) < 8:
        print("Tamanho mínimo de 8 caracteres.")

#Contabiliza os tipos de caracteres encontrados
for caracter in senha:
    if caracter.isupper():
        maiusculo += 1
    elif caracter.islower():
        minusculo += 1
    elif caracter.isdigit():
        numeral += 1
    elif caracter.isspace():
        espaco += 1
    elif caracter in ("@", "#","$", "%", "&"):
        caracter_especial += 1

if maiusculo == 0 or minusculo == 0 or numeral == 0 or caracter_especial == 0 or espaco > 0:
    resultado = "Senha inválida"
else:
    resultado = "Senha válida"

print("===== ANÁLISE DA SENHA =====")
print(f"Usuário: {nome}")
#Tamanho esta com OK ja incluco pois tem um validador anterior que impede de chgar ao final sem no minimo 8 digitos
print(f"Tamanho mínimo: OK")
#Condicionais que apontam a conformidade ou não conformidade dos itens
if maiusculo == 0:
    print("Letra maiúscula: NÃO ATENDIDO")
else:
    print("Letra maiúscula: OK")

if minusculo == 0:
    print("Letra minúscula: NÃO ATENDIDO")
else:
    print("Letra minúscula: OK")

if numeral == 0:
    print("Número: NÃO ATENDIDO")
else:
    print("Número: OK")

if espaco > 0:
    print("Sem espaços: NÃO ATENDIDO")
else:
    print("Sem espaços: OK")

if caracter_especial == 0:
    print("Caracter especial: NÃO ATENDIDO")
else:
    print("Caracter especial: OK")

print(f"Resultado: {resultado}")
