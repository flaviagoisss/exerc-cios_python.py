print('\t---contegem dos digitos---')
digitos = int(input("digite um numero para contar seus digitos: "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador += 1
print("total de digitos = ", contador)
print("\n")

#-----------------------------------#
print('\t---a dança dos numeros---')
x = int(input("informe um numero para brincar:"))
if x < 0:
    print('e um umero negativo')
elif x == 0:
    print('e um numero neutro')
elif x == 0:
    print('e um numero positivo')
print("\n")

#--------------------------------------#
print('\t---soma de 1 ate o valor digitado---')
soma_numeros = 0
numero = int(input("por favor, insira um numero:"))
for i in range(1, 1):
    soma_numeros += i
print("a soma é ", soma_numeros)
print("\n")

#-------------------------------------#
print('\t--numero entre 5 e 100 que são divisiveis por 7--')
for num in range(5, 100):
    if (num % 7 == 0 and num % 5 != 0):
        print(num)
print("\n")

#--------------exemplo2---------------#
print('\n\t---calculo do novo salario---')
salario_atual = float(input('informe o salario atual: '))

if (salario_atual < 500):
    salario_novo = salario_atual + (salario_atual * 0.15)
    print('salario com rejuste =', salario_novo)

if ((salario_atual >= 500) and (salario_atual <= 1000)):
    salario_novo = salario_atual + (salario_atual * 0.10)
    print('salario com rejuste =', salario_novo)

if (salario_atual > 1000):
    salario_novo = salario_atual + (salario_atual * 0.05)
    print('salario com rejuste =', salario_novo)

#---------------exemplo1--------------#
print('\n\t-----tabuada------')
numero = int(input('informe o numero para ver a tabuada:'))

print('\ntabuada de', numero, ":")

for i in range(1, 11):
    print(numero, 'x', i, '=', (numero * i))
print("\n")
