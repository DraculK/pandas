# Pandas 🐼
Para começar a utilizar a biblioteca pandas é necessário, primeiramente, importar e para isso podemos usar o código:   
~~~python
import pandas as pd
~~~
Nesse caso, importamos a biblioteca pandas e utilizamos pd como uma abreviação que será usada sempre que precisarmos de alguma funcionalidade da biblioteca. Por exemplo:   
~~~python
import pandas as pd
df = pd.read_csv('file.csv')
df
~~~
Nesse código, utilizamos a funcionalidade de ler arquivo csv utilizando a abreviação pd que definimos quando informamos o pandas. Então, pegamos o que lemos desse csv e adicionamos a uma variável df (abreviação de Data Frame) e depois, ao digitar df, imprimimos o que tem no arquivo csv.   
Alguns outros comandos mais básicos que podemos utilizar:   
~~~python
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
~~~
***OBS***: lembrando que todos os df que utilizamos nos exemplos, são, idealmente, tabelas com dados.
