# Dia 5 — Sistema de fechamento de compra

## Objetivo

Desenvolver um programa que registre os produtos de uma compra, calcule o subtotal, aplique o desconto correspondente e apresente um resumo ao cliente.

Este desafio revisa os principais conteúdos praticados nos quatro primeiros dias.

## Requisitos

O programa deverá solicitar:

1. nome do cliente;
2. quantidade de produtos diferentes;
3. nome de cada produto;
4. preço unitário;
5. quantidade comprada.

## Validações

O programa deverá verificar se:

- a quantidade de produtos diferentes é maior que zero;
- o preço unitário é maior que zero;
- a quantidade comprada é maior que zero;
- a forma de pagamento corresponde a uma opção válida.

Quando um valor inválido for informado, o programa deverá mostrar uma mensagem de erro e solicitar o dado novamente.

## Cálculos

O total de cada produto será calculado por:

```text
total do produto = preço unitário × quantidade comprada
```

O subtotal será formado pela soma do total de todos os produtos:

```text
subtotal = soma dos totais dos produtos
```

O programa também deverá calcular a quantidade total de unidades compradas.

## Regras de desconto

| Subtotal | Desconto |
|---:|---:|
| Menor que R$ 100,00 | 0% |
| De R$ 100,00 até R$ 299,99 | 5% |
| De R$ 300,00 até R$ 499,99 | 10% |
| R$ 500,00 ou mais | 15% |

Depois de identificar o percentual, o programa deverá calcular:

```text
valor do desconto = subtotal × percentual
valor final = subtotal - valor do desconto
```

## Formas de pagamento

O programa deverá apresentar as seguintes opções:

```text
1 — Dinheiro
2 — Cartão
3 — Pix
```

Somente os números `1`, `2` e `3` serão aceitos.

## Saída esperada

Ao final, o programa deverá apresentar um resumo semelhante a este:

```text
===== RESUMO DA COMPRA =====
Cliente: Emanuel
Quantidade de produtos diferentes: 2
Total de unidades: 9
Subtotal: R$300.00
Desconto aplicado: 10%
Valor do desconto: R$30.00
Valor final: R$270.00
Pagamento no Pix.
```

## Conceitos praticados

- entrada de dados com `input()`;
- conversão com `int()` e `float()`;
- estruturas condicionais;
- estruturas de repetição `for` e `while`;
- validação de dados;
- operadores relacionais;
- operador de pertencimento `not in`;
- contadores;
- acumuladores;
- listas e `append()`;
- cálculos de porcentagem;
- formatação monetária com f-strings.

## Desafio extra

Adicionar a escolha da forma de pagamento e validar para que somente as opções `1`, `2` e `3` sejam aceitas.

## Melhoria futura

Criar uma nota detalhada contendo, para cada produto:

- nome;
- preço unitário;
- quantidade;
- total do produto.

Essa melhoria será realizada futuramente, depois do estudo mais aprofundado de listas e dicionários.

## Critérios de conclusão

O desafio será considerado concluído quando o programa:

- cadastrar a quantidade definida de produtos;
- rejeitar preços e quantidades inválidas;
- somar corretamente todas as unidades;
- calcular o subtotal;
- aplicar o desconto adequado;
- calcular o valor final;
- validar a forma de pagamento;
- apresentar o resumo da compra.

## Estrutura da pasta

```text
dia-005/
├── dia05.md
└── dia05.py
```

## Status

Desafio concluído ✅