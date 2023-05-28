print('\n **************Escolha a operação****************')

print("""
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
""")

user_input = int(input())

numero1 = int(input('\n Digite o primeiro número: '))
numero2 = int(input('\n Digite o segundo número: '))

match user_input:
    case 1:
        resultado = numero1 + numero2
    case 2:
        resultado = numero1 - numero2
    case 3:
        resultado = numero1 * numero2
    case 4:
        resultado = numero1 / numero2       
    case _:
        print('operação inválida')


print('O Resultado é ', resultado)

