# Dia 4 — Analisador de notas

## Objetivo

Desenvolver um programa capaz de receber as notas de um estudante, calcular sua média e informar sua situação final.

O desafio foi utilizado para praticar estruturas de repetição, contadores, acumuladores, validação de dados e estruturas condicionais.

## Funcionamento

O programa solicita:

1. nome do estudante;
2. nome da disciplina;
3. quantidade de avaliações;
4. nota de cada avaliação.

Depois de receber todas as notas válidas, o programa calcula:

- a soma das notas;
- a média final;
- a situação do estudante.

## Regras

- A quantidade de avaliações deve ser maior que zero;
- Cada nota deve estar entre `0` e `10`;
- Uma nota inválida não pode ser adicionada à soma;
- Quando uma nota inválida for digitada, o programa deve solicitá-la novamente;
- O contador só deve avançar depois que uma nota válida for informada.

## Critérios de classificação

| Média final | Situação |
|---:|---|
| Menor que 5 | Reprovado |
| De 5 até menos de 7 | Recuperação |
| 7 ou mais | Aprovado |

## Conceitos praticados

Neste desafio foram utilizados:

- entrada de dados com `input()`;
- conversão de dados com `int()` e `float()`;
- estrutura de repetição `while`;
- estrutura condicional `if`, `elif` e `else`;
- comando `continue`;
- contador;
- acumulador;
- operadores relacionais;
- operadores lógicos;
- formatação com f-strings;
- formatação de números decimais.

## Contador

A variável `i` foi utilizada para controlar qual avaliação está sendo solicitada:

```python
i = 1
```

Depois de receber uma nota válida, o contador é incrementado:

```python
i += 1
```

O contador não é incrementado quando a nota é inválida. Dessa forma, o programa solicita novamente a mesma avaliação.

## Acumulador

A variável `notas` começa com o valor zero:

```python
notas = 0
```

Cada nota válida é adicionada ao total:

```python
notas += nota
```

Ao final da repetição, essa variável contém a soma de todas as notas.

## Validação das notas

A seguinte condição verifica se a nota está fora do intervalo permitido:

```python
if nota < 0 or nota > 10:
```

Quando isso acontece, o comando `continue` retorna ao começo do `while`:

```python
print("Nota inválida! Digite um número entre 0 e 10.")
continue
```

Como o contador ainda não foi incrementado, o programa solicita novamente a mesma nota.

## Exemplo de execução

```text
Digite o nome do estudante: emanuel
Digite a disciplina: python
Digite a quantidade de avaliações: 3
Digite a 1ª nota: 8
Digite a 2ª nota: 15
Nota inválida! Digite um número entre 0 e 10.
Digite a 2ª nota: 7.5
Digite a 3ª nota: 7

===== RESULTADO FINAL =====
Estudante: Emanuel
Disciplina: Python
Quantidade de avaliações: 3
Soma das notas: 22.50
Média final: 7.50
Situação: Aprovado
```

## Principais aprendizados

Durante o desafio, aprendi que:

- o `while` repete um bloco enquanto sua condição for verdadeira;
- um contador controla a quantidade de repetições;
- um acumulador guarda a soma dos valores;
- o `continue` retorna ao início da repetição atual;
- o contador deve avançar somente depois que a entrada for validada;
- validar os dados antes dos cálculos evita resultados incorretos;
- a ordem e a indentação dos comandos alteram o funcionamento do programa.

## Possíveis melhorias

Em versões futuras, o programa poderá:

- tratar entradas que não sejam números;
- armazenar as notas em uma lista;
- mostrar a maior e a menor nota;
- calcular quantas notas ficaram acima da média;
- permitir o cadastro de vários estudantes;
- separar as partes do programa em funções.

## Estrutura da pasta

```text
dia-004/
├── dia04.md
└── dia04.py
```

- `dia04.md`: descrição e regras do desafio;
- `dia04.py`: código desenvolvido;
- `README.md`: documentação e registro dos aprendizados.

## Status

Desafio concluído ✅