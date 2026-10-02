# Dia 6 — Validador de senha

## Objetivo

Desenvolver um programa que analise uma senha e informe se ela atende aos requisitos mínimos de segurança.

O desafio foi utilizado para praticar strings, estruturas de repetição, métodos de caracteres, contadores e operadores lógicos.

## Requisitos da senha

Para ser considerada válida, a senha deverá possuir:

- pelo menos 8 caracteres;
- pelo menos uma letra maiúscula;
- pelo menos uma letra minúscula;
- pelo menos um número;
- pelo menos um caractere especial;
- nenhum espaço.

## Caracteres especiais aceitos

```text
@ # $ % &
```

## Entrada

O programa deverá solicitar:

1. nome do usuário;
2. senha que será analisada.

Se a senha possuir menos de oito caracteres, o programa deverá solicitar uma nova senha.

## Processamento

O programa deverá percorrer cada caractere da senha e identificar se ele é:

- uma letra maiúscula;
- uma letra minúscula;
- um número;
- um espaço;
- um caractere especial permitido.

Para isso, poderão ser utilizados:

```python
caractere.isupper()
caractere.islower()
caractere.isdigit()
caractere.isspace()
```

A presença do caractere especial poderá ser verificada com:

```python
caractere in "@#$%&"
```

## Resultado esperado

O programa deverá apresentar um relatório semelhante a este:

```text
===== ANÁLISE DA SENHA =====
Usuário: Emanuel
Tamanho mínimo: OK
Letra maiúscula: OK
Letra minúscula: OK
Número: OK
Sem espaços: OK
Caractere especial: OK
Resultado: Senha válida
```

Quando algum requisito não for atendido:

```text
===== ANÁLISE DA SENHA =====
Usuário: Emanuel
Tamanho mínimo: OK
Letra maiúscula: NÃO ATENDIDO
Letra minúscula: OK
Número: NÃO ATENDIDO
Sem espaços: OK
Caractere especial: OK
Resultado: Senha inválida
```

## Testes recomendados

| Senha | Resultado esperado |
|---|---|
| `python` | Inválida: menos de 8 caracteres |
| `Python@abc` | Inválida: não possui número |
| `python@123` | Inválida: não possui maiúscula |
| `PYTHON@123` | Inválida: não possui minúscula |
| `Python 123@` | Inválida: contém espaço |
| `Python123` | Inválida: não possui caractere especial |
| `Python@123` | Válida |

## Conceitos praticados

- strings;
- função `len()`;
- estrutura de repetição `for`;
- estrutura de repetição `while`;
- métodos de strings;
- contadores;
- estruturas condicionais;
- operadores `and` e `or`;
- operador de pertencimento `in`;
- validação de dados.

## Principais aprendizados

Neste desafio foi possível aprender que:

- uma string pode ser percorrida caractere por caractere;
- métodos de string ajudam a identificar diferentes tipos de caracteres;
- contadores podem registrar quantas vezes cada requisito aparece;
- basta um requisito não ser atendido para a senha ser considerada inválida;
- o `while` pode impedir que o programa continue com uma senha muito curta;
- o operador `in` permite verificar se um valor pertence a um conjunto de opções.

## Melhoria futura

Fazer o programa solicitar uma nova senha enquanto qualquer requisito não for atendido.

Também será possível:

- contar o número de tentativas;
- impedir que características de tentativas diferentes sejam acumuladas;
- classificar a senha como fraca, média ou forte;
- ocultar a senha durante a digitação.

## Critérios de conclusão

O desafio será considerado concluído quando o programa:

- impedir senhas com menos de oito caracteres;
- percorrer todos os caracteres;
- identificar letras maiúsculas e minúsculas;
- identificar números;
- identificar espaços;
- identificar caracteres especiais;
- informar quais requisitos foram atendidos;
- apresentar o resultado final.

## Estrutura da pasta

```text
dia-006/
├── dia06.md
└── dia06.py
```

## Status

Desafio concluído ✅