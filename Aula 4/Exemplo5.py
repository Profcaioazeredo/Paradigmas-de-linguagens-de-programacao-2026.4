print("Sistema Cinema UVA")
idade = int(input("Insira a sua idade:"))
# Pedindo idade para o usuário
if (idade < 18): #Condicional, apenas se a condição for satisfeita o código com o espaçamento após ele, executará
    print("Tem direito a meia entrada") # Esse print somente executará caso a idade seja menor que 18
else:
    print("Não tem direito a meia entrada") #Esse código executará somente se a idade for maior ou igual a 18 anos
print("Sistema finalizado") # Esse print não está dentro do if, ele executará independentemente 