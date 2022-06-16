'''Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.
'''

fat = {'São Paulo': 67836.43,
       'Rio de Janeiro': 36678.66,
       'Minas Gerais': 29229.88,
       'Espírito Santo': 27165.48,
       'Outros': 19849.53}
tot = sum(fat.values())
print(f'O faturamento mensal total foi de R${tot}')

for k, v in fat.items():
    print(f'A participação de {k} no faturamento mensal é de {(v * 100) / tot:.2f}%')
