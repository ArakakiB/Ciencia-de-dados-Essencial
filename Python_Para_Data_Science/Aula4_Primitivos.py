'''
str - String - Cadeia de textos
int - Inteiro - Numeros nao facionados positivos e negativos
float - FLutuante - Numeros quebrados positivos e negativos
bool - Booleano - True/False
'''

print(type("Qualquer coisa String"))  # O type diz qual é o tipo de dado
print(type(10.5))  # float
# O bool se estiver vazio ou com 0 retorna sempre false
# EX.:
print(bool(0))
# Aqui estou fazendo um type casting, que é converter um tipo em outro, nesse caso string em bool
print(bool("Luiz"))  # Aqui ele retorna True porque a string tem valor

print(bool(""))  # Como aqui a string nao tem valor, ele me retorna False

# Outro exemplo de Type Casting
print(type(int("10")))  # Aqui só coloquei o type para mostrar que converteu para int. Mas perceba que dentro do int eu coloquei uma string

# Exemplo de comparação com booleano
print(bool(10 == 10))
