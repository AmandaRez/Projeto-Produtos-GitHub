#Solicite uma string e um número inteiro como entrada. Retorne a string repetida o número de vezes informado.

print("Bem-vind@! Este programa serve para repetir uma string um determinado número de vezes.")
string = input("Informe a string: ")
numero = int(input("Informe o número de vezes que deseja repetir a string: "))
resultado = string * numero
print(f"A string '{string}' repetida {numero} vezes é: {resultado}")
print("Obrigado por usar o programa!")