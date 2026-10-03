palindromo = input("Digite uma palavra:").strip().lower()
while not palindromo:
    print("A palavra não pode estar vazia.")
    palindromo = input("Digite uma palavra:").strip()
"""
Como inicialmente havia feito
for i in range(len(palavra)):
    palindromo += palavra[(i+1)*-1]

"""

if palindromo == palindromo[::-1]:
    print(f"{palindromo.capitalize()} é um palíndromo")
else:
    print(f"{palindromo.capitalize()} não é um palíndromo")