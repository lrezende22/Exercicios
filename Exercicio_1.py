# Enunciado: Calcule a soma entre todos os números impares que
# são multiplos de 3 e que se encontram no intervalo de 1 até 500

n = 1000
soma = 0
cont = 0

for c in range(1,n):
  if c % 3 == 0 or c % 5 == 0:  #divisivel por 3 ou por 5
    soma = c + soma
    cont = cont + 1
print('A soma de todos os {} valores é igual {}'.format(cont,soma))