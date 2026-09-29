# Dia 3 — Controle de acesso a evento

## Objetivo

Desenvolver um programa que determine se uma pessoa pode entrar em um evento com base em sua idade, na posse de um ingresso e, quando necessário, na presença de um responsável.

Este desafio foi utilizado para praticar estruturas condicionais, operadores lógicos, validação de dados e organização do fluxo de execução de um programa.

## Regras de acesso

O programa utiliza as seguintes regras:

- Pessoas com menos de 16 anos não podem entrar;
- Pessoas de 16 ou 17 anos precisam:
  - possuir ingresso;
  - estar acompanhadas de um responsável;
- Pessoas com 18 anos ou mais precisam possuir ingresso;
- Idades negativas são consideradas inválidas;
- As respostas relacionadas ao ingresso e ao responsável devem ser `s` ou `n`.

## Funcionamento do programa

O programa solicita:

1. nome da pessoa;
2. idade;
3. confirmação de que possui ingresso;
4. confirmação da presença de um responsável, quando a pessoa possui 16 ou 17 anos.

Depois, o programa apresenta o resultado do controle de acesso, informando se a entrada foi permitida ou negada e, quando necessário, o motivo da recusa.

## Conceitos praticados

Durante o desenvolvimento deste desafio, foram utilizados:

- entrada de dados com `input()`;
- conversão de texto para número com `int()`;
- estruturas condicionais `if`, `elif` e `else`;
- estruturas condicionais aninhadas;
- operadores de comparação;
- operadores de pertencimento `in` e `not in`;
- validação de dados;
- formatação de textos com f-strings;
- métodos de strings como `.lower()` e `.capitalize()`.

## Validações implementadas

O programa verifica:

- se a idade informada é negativa;
- se a resposta sobre o ingresso é `s` ou `n`;
- se a resposta sobre o responsável é `s` ou `n`;
- se a pessoa atende aos requisitos de idade;
- se a pessoa possui ingresso;
- se um menor de 18 anos está acompanhado.

## Cenários testados

| Idade | Ingresso | Responsável | Resultado |
|---:|:---:|:---:|---|
| 15 | — | — | Entrada negada por idade |
| 17 | Sim | Não | Entrada negada por falta de responsável |
| 17 | Sim | Sim | Entrada permitida com responsável |
| 30 | Não | — | Entrada negada por falta de ingresso |
| 30 | Sim | — | Entrada permitida |

## Principais aprendizados

### A ordem das condições é importante

A verificação de idade negativa precisa acontecer antes da condição `idade < 16`. Isso ocorre porque uma idade negativa também é menor que 16.

```python
if age < 0:
    print("Valor inválido.")
elif age < 16:
    print("Entrada negada.")
```

### Métodos precisam de parênteses

Para executar métodos como `lower` e `capitalize`, é necessário utilizar parênteses:

```python
name = input("Digite seu nome: ").capitalize()
ticket = input("Possui ingresso? (s/n): ").lower()
```

Sem os parênteses, a variável recebe uma referência ao método, e não o texto transformado.

### Validação de várias opções

A expressão abaixo não realiza a validação corretamente:

```python
if ticket == "s" or "n":
```

A forma utilizada no projeto foi:

```python
if ticket not in ("s", "n"):
    print("Dados inválidos.")
```

Dessa forma, o programa verifica se a resposta não pertence ao conjunto de alternativas permitidas.

## Estrutura da pasta

```text
dia-003/
├── dia03.md
├── dia03.py
└── README.md
```

- `dia03.md`: descrição e regras do desafio;
- `dia03.py`: implementação do programa;
- `README.md`: documentação dos conceitos e aprendizados.

## Possíveis melhorias

Em versões futuras, o programa poderá receber:

- repetição da pergunta quando o usuário informar uma opção inválida;
- tratamento de erro quando a idade não for um número;
- redução da repetição dos comandos `print`;
- separação da lógica em funções;
- registro de várias pessoas em uma mesma execução.

## Status

Desafio concluído ✅
