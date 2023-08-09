'''
Manipulando cadeia de texto
'''

'''
Fatiamento de uma string
'''
# É conseguir pegar uma parte de uma string

# Exenplo
frase = "Curso em Vídeo Python" # Uma frase com 21 espaços(o 0 conta e os espaços também)
frase[9] # Será selecionado o espaço 9, no caso a letra: "V".
frase[9:13] # Será selecionado da letra 9 até 12, porque o ultimo número entra na contagem.
frase[9:21:2] # Vai comeceçar no 9, vai até o 20, mas vai pulando de dois em dois.
frase[:5] # Vai começar no espaço 0, e vai até o espaço 4.
frase[15:] # Vai começar do espaço 15, e vai até o ultim espaço.
frase[9::3] # Vai começar no espaço 9, vai até o final da frase, pulando de 3 em 3.

'''
Análise
'''

# Saber informações da string

# Exemplos

len(frase) # Comprimento. Mostra o comprimento da frase, no caso vai motras que tem 21 espaços
frase.count("o") # Conta quantas vezes tem a letra que eu quero saber. No caso 3 letras "o"
frase.count("o", 0, 13) # Para saber quantas letras "o" tem no inicio do espaço 0 até o espaço 12
frase.find("deo") # Vai mostrar aonde esta as letras no espaço, no caso, está no espaço 11 até o 14
frase.find("Android") # Vai retornar o espaço -1, porque não existe essa palavra ou letra, string de baixo
"Curso" in frase # Aqui eu pergunto se existe curso escrito na frase, ele vai me informar se é verdadeiro ou falso. No caso aqui é verdadeiro.

'''
Transformação
'''
# Uma regra: Uma lista de string, ela é imutavel, a gente não consegue mexer nela, mas conseguimos mudar

frase.replace("Python", "Android") # Aqui eu quero que ele pegue a palavra python, e mude para android.
frase.upper() # Vai ficar em maiusculo, toda a frase.
frase.lower() # Vai deixar em minusculo, toda a frase.
frase.capitalize() # Vai deixar tudo minusculo, e depois vai colocar a primeira letra maiuscula
frase.title() # Vai analisar quantas palavras a frase tem. E colocar a primeira letra de cada palavra em maiusculo.

# Vamos colocar uma frase nova

frase2 = "   Aprenda Python  "
frase2.strip() # Ele vai remover todos os espaços inuteis, no inicio e no fim da frase
frase2.rstrip() # Ele remove so espaços da direita, no caso, do final da frase
frase2.lstrip() # Ele remove so os espaços da esquerda, no caso, do camoeço da frase

'''
Divisão
'''
# Voltamos a usar a primeira frase que foi escrita

frase.split() # Ele cria uma lista para cada palavra escrita na sua frase

# Exemplo:

# frase = "Curso em video python"
# tem 21 caracteres, no caso, começa no 0 e vai até o 20
# usando o split, vai acontecer isso ó
# curso em video python
# 01234 01 01234 012345
# criou uma lista para cada palavra.
# A palavra 0 é: "curso", a palavra 1 é: "em", a palavra 2 é: "video", a palavra 3 é: "python"

'''
Junção
'''
# se eu tenho palavras separadas em listas, eu pósso juntar

"-".join(frase) # Vai juntar tudo com separador que eue escrevi: "Curso-em-Vídeo-Python"
" ".join(frase) # Caso você queira que a junção seja com espaço: "Curso em Vídeo Python"

'''
Em Python (e em muitas outras linguagens de programação), as listas são indexadas começando do zero. Isso significa que o primeiro elemento de uma lista tem o índice 0, o segundo elemento tem o índice 1, o terceiro tem o índice 2 e assim por diante.

Quando usamos -1 como índice, estamos acessando o último elemento da lista. O uso de índices negativos é uma característica muito útil em Python, pois permite que você acesse elementos da lista de trás para frente.

Por exemplo, considere a lista nomes com os valores ['Ana', 'Maria', 'de', 'Souza']:

nomes[0] retorna 'Ana'
nomes[1] retorna 'Maria'
nomes[2] retorna 'de'
nomes[3] retorna 'Souza'
nomes[-1] retorna 'Souza'
nomes[-2] retorna 'de'
nomes[-3] retorna 'Maria'
nomes[-4] retorna 'Ana'
Portanto, usar nomes[-1] é uma forma conveniente de obter o último elemento da lista, independentemente do seu tamanho, sem precisar saber o número exato de elementos na lista. Nesse caso específico, usamos -1 para acessar o último nome da lista nomes e considerá-lo como o último nome completo da pessoa.

'''
