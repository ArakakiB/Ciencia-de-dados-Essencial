print("John", "Doe")  # Aqui como podemos ver, por padrao o Python separa os argumentos com um espaco
print("John", "Doe", sep="-")  # Porem, eu posso usar o "sep" (separador), para escolher com que caracter eu quero separar os argumentos
# A cima tambem podemos reparar que por padrao o Python da uma quebra de linha entre os prints

print("John", "Doe", sep="", end="")  # Consigo tambem escolher qual caracter eu quero substituir pela quebra de linha utilizando o comando end
print("John", "Doe", sep="+", end="*")
print("John", "Doe", end="#")
print("John", "Doe")

# Teste com CPF 444.666.555-11

print("444", "666", "555", sep=".", end="-")
print("11")




















