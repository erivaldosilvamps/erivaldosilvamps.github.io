n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira: '))
m = ((n1+n2+n3)/3)
print('A média do aluno é {:.1f}'.format(m))
if m>=7:
    print('Parabens!! você foi a provado'),
else: print('Ifelizmente terá que ir para a final')

