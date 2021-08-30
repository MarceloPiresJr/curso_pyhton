nome = "Marcelo Pires"
idade = 29
peso = 74
altura = 1.80
e_maior =  idade > 18
imc =  peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))