'''
Alguns conceitos a mais sobre Aritmética
'''

# Alguns sinais que você conhece

" + " # Adição
" - " # Subtração
" * " # Multiplicação
" / " # Divisão
" ** " # Potência
" // " # Divisão Inteira
" % " # Resto da Divisão
'''
5 + 2 = 7
5 - 2 = 3
5 * 2 = 10
5 / 2 = 2.5
5 ** 2 = 25
5 // 2 = 2
5 % 2 = 1
'''

'''
Ordem de precedência  
'''
# A primeira coisa a ser calculada são:
"()" # usa só parenteses em aritmétricas, e são o primeiro a calcular

# A segunda é:
"**"
# A terceira:
"*, /, //, %"

# A quarta:
"+, -"

'''
Exemplos
'''

5 + 3 * 2 = 11 # A multiplicação vem primeiro comparado a soma

3 * 5 + 4 **2 = 31
# A pontecialização vem primeiro comparado a multiplicação, 
# e só depois a soma, já que está em ultimo em prioridade

3 * (5 + 4) **2 = 243
# Primeiro tudo que está em parenteses, depois potencia, multiplicação e só depois soma
# mas nesse caso a soma foi primeiro, pois, ela estava dentro do parenteses.

