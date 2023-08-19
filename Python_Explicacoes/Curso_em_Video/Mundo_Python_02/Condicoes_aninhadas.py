'''
Condições aninhadas em Python referem-se à estrutura onde você tem uma instrução
condicional dentro de outra instrução condicional. Isso permite que você execute
diferentes blocos de código dependendo de várias condições.
As condições aninhadas são geralmente implementadas usando a estrutura "if-elif-else".
'''
# Operadores usados

# Operador "and" (E lógico):
'''
O operador "and" é usado para combinar duas ou mais condições, e a expressão
resultante é verdadeira apenas se todas as condições forem verdadeiras

idade = 25
tem_cartao = True

if idade >= 18 and tem_cartao:
    print("Você pode entrar na festa.")
else:
    print("Desculpe, você não pode entrar.")
'''

# Operador "or" (OU lógico):
'''
O operador "or" é usado para combinar duas ou mais condições,
e a expressão resultante é verdadeira se pelo menos uma das condições for verdadeira.

tem_carteira = True
tem_celular = False

if tem_carteira or tem_celular:
    print("Você tem pelo menos um dos itens necessários.")
else:
    print("Você não tem nenhum dos itens necessários.")
'''

# Operador "not" (NÃO lógico):
'''
O operador "not" é usado para negar uma condição.
Ele reverte o valor da condição, tornando o verdadeiro falso e o falso verdadeiro.

idade = 15

if not idade >= 18:
    print("Você é menor de idade.")
else:
    print("Você é maior de idade.")
'''
