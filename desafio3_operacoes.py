# Solicite dois números inteiros e execute uma operação simples entre eles.

print("Bem-vind@! Este programa serve para somar dois números inteiros.")
numero1 = int(input("Informe o primeiro número inteiro: "))
numero2 = int(input("Informe o segundo número inteiro: "))  
operacao = input("Informe a operação desejada (+, -, *, /): ")

if operacao == "+": 
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
elif operacao == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: Divisão por zero não é permitida."
else:   
    resultado = "Erro: Operação inválida."
print(f"O resultado da operação {numero1} {operacao} {numero2} é: {resultado}")
print("Obrigado por usar o programa!")









