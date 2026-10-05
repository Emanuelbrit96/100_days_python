# Dia 9 — Cadastro e análise de produtos

## Objetivo

Desenvolver um programa que cadastre produtos e preços em listas, relacione os dados por meio dos índices e apresente uma análise dos valores cadastrados.

Este desafio introduz o uso estruturado de listas em Python.

## Estrutura dos dados

O programa deverá utilizar duas listas:

```python
produtos = []
precos = []
```

O produto e seu preço deverão ocupar a mesma posição nas duas listas.

Exemplo:

```python
produtos = ["Café", "Leite", "Pão"]
precos = [18.50, 7.00, 8.50]
```

Nesse exemplo:

- `produtos[0]` corresponde a `precos[0]`;
- `produtos[1]` corresponde a `precos[1]`;
- `produtos[2]` corresponde a `precos[2]`.

## Entrada

O programa deverá solicitar:

1. quantidade de produtos que serão cadastrados;
2. nome de cada produto;
3. preço de cada produto.

## Validações

O programa deverá verificar se:

- a quantidade de produtos é maior que zero;
- o nome do produto não está vazio;
- o preço não está vazio;
- o preço é maior que zero.

Quando uma entrada for inválida, o programa deverá mostrar uma mensagem e solicitar novamente o mesmo dado.

Somente produtos e preços válidos deverão ser adicionados às listas.

## Cadastro dos produtos

O cadastro deverá seguir o formato:

```text
Produto 1 de 3
Nome: Café
Preço: 18.50
```

Os dados serão adicionados com:

```python
produtos.append(produto)
precos.append(preco)
```

## Relatório dos produtos

Depois do cadastro, o programa deverá apresentar uma lista numerada:

```text
===== PRODUTOS CADASTRADOS =====
1. Café — R$18.50
2. Leite — R$7.00
3. Pão — R$8.50
```

Para relacionar cada produto ao seu preço, o programa poderá percorrer os índices:

```python
for i in range(len(produtos)):
```

## Análise dos preços

O programa deverá calcular:

- quantidade de produtos cadastrados;
- soma dos preços;
- preço médio;
- maior preço;
- menor preço;
- produto mais caro;
- produto mais barato;
- quantidade de produtos com preço igual ou superior a R$ 10,00.

## Funções utilizadas

### Quantidade de elementos

```python
len(produtos)
```

### Soma dos preços

```python
sum(precos)
```

### Maior preço

```python
max(precos)
```

### Menor preço

```python
min(precos)
```

### Posição de um preço

```python
precos.index(valor)
```

A posição encontrada na lista `precos` poderá ser utilizada para acessar o produto correspondente na lista `produtos`.

Exemplo conceitual:

```python
maior_preco = max(precos)
posicao = precos.index(maior_preco)
produto_mais_caro = produtos[posicao]
```

Se existirem preços repetidos, `.index()` retornará a posição da primeira ocorrência.

## Exemplo de saída

```text
===== PRODUTOS CADASTRADOS =====
1. Café — R$18.50
2. Leite — R$7.00
3. Pão — R$8.50

===== ANÁLISE =====
Quantidade de produtos: 3
Soma dos preços: R$34.00
Preço médio: R$11.33
Produto mais caro: Café — R$18.50
Produto mais barato: Leite — R$7.00
Produtos com preço igual ou superior a R$10.00: 1
```

## Conceitos praticados

- criação de listas;
- método `.append()`;
- índices;
- relação entre listas;
- função `len()`;
- função `sum()`;
- funções `min()` e `max()`;
- método `.index()`;
- repetição com `for`;
- validação com `while`;
- contadores;
- formatação monetária;
- organização e limpeza do código.

## Principais aprendizados

Neste desafio foi possível aprender que:

- listas armazenam vários valores em uma única variável;
- os índices começam na posição zero;
- listas diferentes podem ser relacionadas pelas posições;
- `.append()` adiciona um elemento ao final da lista;
- `sum()` substitui um acumulador quando queremos apenas somar valores;
- `min()` e `max()` encontram os extremos de uma sequência;
- `.index()` retorna a posição da primeira ocorrência;
- entradas devem ser validadas antes de serem adicionadas;
- valores iniciais arbitrários, como `menor_preco = 10000`, podem causar erros;
- códigos antigos não precisam permanecer comentados porque o Git preserva o histórico.

## Testes recomendados

Testar:

- quantidade igual a zero;
- quantidade negativa;
- nome vazio;
- preço vazio;
- preço igual a zero;
- preço negativo;
- somente um produto;
- vários produtos;
- preços abaixo e acima de R$ 10,00;
- dois produtos com o mesmo preço;
- todos os produtos com preços elevados.

## Limitação atual

Se forem digitadas letras em uma entrada numérica, o programa poderá apresentar `ValueError`.

Essa situação será tratada futuramente com:

```python
try
except
```

## Desafio extra

Solicitar o nome de um produto e pesquisar se ele está cadastrado.

Quando for encontrado:

```text
Produto encontrado: Café — R$18.50
```

Quando não for encontrado:

```text
Produto não encontrado.
```

A busca não deverá diferenciar letras maiúsculas e minúsculas.

Exemplos equivalentes:

```text
café
Café
CAFÉ
```

## Melhorias futuras

O programa poderá futuramente:

- utilizar uma lista de dicionários;
- guardar quantidade e categoria;
- permitir edição e remoção;
- pesquisar vários produtos;
- ordenar os produtos pelo preço;
- salvar os dados em arquivo;
- tratar entradas inválidas com exceções.

## Critérios de conclusão

O desafio será considerado concluído quando o programa:

- validar a quantidade de produtos;
- impedir nomes vazios;
- impedir preços vazios ou menores que zero;
- adicionar os dados às listas;
- relacionar corretamente produtos e preços;
- apresentar os produtos cadastrados;
- calcular soma e média;
- identificar os produtos mais caro e mais barato;
- contar os produtos com preço igual ou superior a R$ 10,00.

## Estrutura da pasta

```text
dia-009/
├── dia009.md
└── dia009.py
```

## Status

Desafio concluído ✅