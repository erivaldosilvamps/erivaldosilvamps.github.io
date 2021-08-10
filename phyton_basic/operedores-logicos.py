#aqui veremos os operadores aritimeticos

n1 = float(input('Digite um numero: '))
n2 = float(input('Digite outro: '))
s = n1+n2
sub = n1-n2
mult = n1*n2
div = n1/n2
poten = n1**n2
div_int = n1//n2
resto_divi = n1%n2
print('A soma vale {}'.format(s))
print('-'*30)
print('A subtração vale {}'.format(sub))
print('-'*30)
print('A multiplicação vale {}'.format(mult))
print('-'*30)
print('A divisão vale {}'.format(div))
print('-'*30)
print('A potencia vale {}'.format(poten))
print('-'*30)
print('A divizão inteira vale {}'.format(div_int))
print('-'*30)
print('O resto da divizção vale {}'.format(resto_divi))

#A ordem de precedência:
# 1 = (), parenteses,
# 2 potencia,
# 3 multiplicação, divisão, divisão inteira, resto da divisão,
# 4 soma e subtração
#ordem de precedencia com parenteses
print('Ordem de precedencia com parenteses')
print('='*30)
print(5+3*2)
print('='*30)
print('Ordem de precedencia com potencia')
print(3*5+4**2)
print('='*30)
print(3*(5+4)**2)

