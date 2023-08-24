'''
Escreva um programa que leia um número n inteiro quelquer e mostre na tela
os n primeiros elementos de uma sequencia de fibonacci.
ex:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''
n = int(input("Digite o valor de n: "))

fibonacci_sequence = []
a, b = 0, 1

for _ in range(n):
    fibonacci_sequence.append(a)
    a, b = b, a + b

print("Sequência de Fibonacci:")
for num in fibonacci_sequence:
    print(num, end=" -> ")

print("...")
