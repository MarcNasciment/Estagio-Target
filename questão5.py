#Escreva um programa que inverta os caracteres de um string.
# a) Essa string pode ser informada através de qualquer entrada de sua preferência
# ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

palavra  = input("Digite uma palavra: ")

def inverter (palavra):
    return palavra [::-1]

print(inverter(palavra))