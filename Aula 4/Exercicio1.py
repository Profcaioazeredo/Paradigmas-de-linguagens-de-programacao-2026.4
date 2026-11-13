# Exercício 1: Crie o arquivo "Exercicio1.py". Esse arquivo deve receber X com o valor 3.2 e Y com o valor 12 no começo do código. Calcule em uma nova variável a Média dos valores, a soma em outra variável e as duas possibilidades de subtração em variáveis diferentes e imprima elas para o usuário. Além disso, comente o código.

# Operadores: 
#       Adição: +
# 	    Subtração: -
# 	    Multiplicação: *
# 	    Divisão: /

x = 3.2
y = 12
soma = x + y
# variavel auxiliar para realizar parte da equação (a soma)
media = x + y /2
# Demonstração de "erro" 
media2 = (x + y)/2
# Calculo direto sem variaveld de apoio
media3 = soma/2
# Calculo com variavel de apoio
print (f"Média calculada errada: {media}")
print (f"Média calculada diretamente: {media2}")
print (f"Média calculada com variavel de apoio: {media3}")
print (f"A soma é {soma}")
subtracao1 = x - y
subtracao2 = y - x
print (f"Subtração 1 {subtracao1}")
print (f"Subtração 2 {subtracao2}")

