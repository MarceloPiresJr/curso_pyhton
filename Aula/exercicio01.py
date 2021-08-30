from datetime import datetime

nome = "Marcelo"
idade = 29
peso = 74.5
altura = 1.80
ano_atual = datetime.now()
e_maior =  idade > 18
imc =  peso / (altura ** 2)
ano_de_nascimento = ano_atual.year - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nascel em {ano_de_nascimento}.')