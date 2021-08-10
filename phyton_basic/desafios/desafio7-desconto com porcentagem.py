
print('='*15)
print('Desconto de 10% para 20 unid\nDesconto de 35% para 50 unid.')
print('Produto 1\n Valor por Unid. R$ 7,50\nProduto 2\n Valor por Unid. R$ 23,99')
print('='*15)
print('Digite 1 Para o produto [1]\ne 2 para para o produto [2]\ncaso queira doar a quantia do desconto do produto 1 digite [3], caso seja, o produto 2 digite [4]')
produto = int(input('Digite a opção: '))
quantidade = int(input('Digite a quantidade: '))
valor1 = 7.50
valor2 = 23.99
total1 = quantidade*valor1
total2 = quantidade*valor2
desconto1 = total1 - (total1 * 10/100)
desconto2 = total2 - (total2 * 35/100)

if produto == 1:
    print('Total R${:.2f}'.format(desconto1))

if produto == 2:
    print('Total R${:.2f}'.format(desconto2))

if produto == 3:
    print('Valor total de R${:.2f} com quantia de desconto no valor de  R${:.2f} enviada para a instituição de caridade'.format(total1, (total1*10/100)))
else:
   print('Valor total de R${:.2f} com quantia de desconto no valor de  R${:.2f} enviada para a instituição de caridade'.format(total2, (total2*35/100)))
