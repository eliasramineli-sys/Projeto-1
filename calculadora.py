# -*- coding: utf-8 -*-
print("Calculadora em Python")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha uma operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input("Digite o número da operação desejada: ")

if opcao == "1":
    resultado = num1 + num2
    print("Resultado da soma:", resultado)

elif opcao == "2":
    resultado = num1 - num2
    print("Resultado da subtração:", resultado)

elif opcao == "3":
    resultado = num1 * num2
    print("Resultado da multiplicação:", resultado)

elif opcao == "4":
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
    else:
        print("Erro: não é possível dividir por zero.")

else:
    print("Opção inválida.")
