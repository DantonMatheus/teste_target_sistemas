'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a
sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de
sua preferência ou pode ser previamente definido no código;'''

n = int(input('Digite um número: '))
fibo = [0, 1, 1]
print('SEQUÊNCIA DE FIBONACCI')
t1 = 0
t2 = 1
t3 = 0
print(f'{t1} --> {t2}', end='')
cont = 3
while t3 <= n:
    t3 = t1 + t2
    if t3 <= n:
        print(f' --> {t3}', end='')
    t1 = t2
    t2 = t3
    cont += 1
    fibo.append(t3)
print(' --> FIM')
if n in fibo:
    print('O valor digitado partence a Sequência de Fibonacci!')
else:
    print('O valor digitado não pertence a Sequência de Fibonacci!')
