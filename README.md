# Pandas

Para começar a utilizar a biblioteca pandas é necessário, primeiramente, importar e para isso podemos usar o código:

```python
import pandas as pd
```

Nesse caso, importamos a biblioteca pandas e utilizamos pd como uma abreviação que será usada sempre que precisarmos de alguma funcionalidade da biblioteca. Por exemplo:

```python
import pandas as pd
df = pd.read_csv('file.csv')
df
```

Nesse código, utilizamos a funcionalidade de ler arquivo csv utilizando a abreviação pd que definimos quando informamos o pandas. Então, pegamos o que lemos desse csv e adicionamos a uma variável **df** (abreviação de Data Frame) e depois, ao digitar df, imprimimos o que tem no arquivo csv.

Alguns outros comandos mais básicos que podemos utilizar:

```python
# Mostra a quantidade de linhas e de colunas
df.shape

# Mostra a quantidade de linhas e de colunas e o tipo de cada coluna 
df.info()

# Permite mostrar um número x de colunas sempre que imprimirmos uma tabela
pd.set_option('display.max_columns', 85)

# Permite mostrar um número x de linhas sempre que imprimirmos uma tabela
pd.set_option('display.max_rows', 85)

# Imprime, por padrão, apenas as primeiras 5 linhas, caso eu passe um parâmetro x nos parênteses, serão mostradas as x primeiras linhas
df.head()

# Funciona igual ao head, no entanto, imprime as x últimas linhas
df.tail(8)
```

---

### Trabalhando com arquivos

```python
# O parâmetro 'r' permite ler tudo que estiver no meu arquivo em questão
open('filename', 'r')

# O parâmetro 'w' permite sobrescrever o que estiver no meu arquivo
open('filename', 'w')

# O parâmetro 'a' permite adicionar algo ao que já está no arquivo
open('filename', 'a')

# Podemos, ainda, concatenar os parâmetros para fazer duas operações de uma vez
open('filename', 'rw')
```

---

### Funções Built-in

- **Map:** aplica uma função a todos os itens de uma lista.

```python
numeros = [1, 2, 3]
quadrado = list(map(lambda x: x*x, numeros)
# quadrado = [2, 4, 6]
```

- **Reduce:** facilita o uso de operações em uma lista como todo.

```python
from functools import reduce
numeros = [1, 2, 3]
soma = reduce(lambda x, y: x + y, numeros)
# soma = 6
```

- **Filter:** cria uma lista de elementos para os quais a função retorna verdadeiro.

```python
numeros = [1, 2, 3]
maior_que_um = list(filter(lambda x: x>1, numeros))
# maior_que_um = [2, 3]
```

- **List Comprehension:** é uma lista, mas no lugar de ser declarada literalmente, servimos uma expressão para a construção dessa lista.
    
    [expressão for valor in coleção], é a forma mais básica da list comprehension.
    
    [expressão for valor in coleção if algo], caso queiramos adicionar condicionais para a criação de uma list comprehension.
    

```python
quadrados = [numero**2 for numero in range(1, 6)]
# quadrados = [1, 4, 9, 16, 25]
quadrados_por_dois = [i**2 for numero in range(1, 6) if numero**2 % 2 == 0]
# quadrados_por_dois = [4, 16]
```

- **Zip:** serve para juntar duas listas, separando o elemento de cada índice em uma tupla, levando em consideração a menor lista.

```python
# mesmo tamanho
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
resultado = list(zip(lista_1, lista_2))
# resultado = [(1, 4), (2, 5), (3, 6)]

# tamanho diferente
lista_1 = [1, 2, 3, 20]
lista_2 = [4, 5, 6]
resultado = list(zip(lista_1, lista_2))
# resultado = [(1, 4), (2, 5), (3, 6)]

# dicionários
dic_1 = {
    'a': 1,
    'b': 2
}
dic_2 = {
    'c': 3,
    'd': 4
}
resultado = list(zip(dic_1, dic_2.values()))
# resultado = [('a', 3), ('b', 4)]
```

- **Enumerate:** adiciona índice a cada elemento de uma lista.

```python
lista = ['C', 'GoLang', 'Python']
resultado = list(enumerate(lista))
# resultado = [(0, 'C'), (1, 'GoLang'), (2, 'Python')]
```
