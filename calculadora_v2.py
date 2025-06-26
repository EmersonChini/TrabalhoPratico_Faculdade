# Variável que armazena a opção do usuário para continuar
saida = ''

# Função que retorna a soma entre dois números
def adicao(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return num1 / num2

# Função que verifica a operação e retorna o resultado
def calculadora(num1, num2, operacao):
    # Deixa a operação minúscula para facilitar a comparação
    operacao = operacao.lower()

    if operacao in ['+', 'adição', 'adicao']:
        resultado = adicao(num1, num2)
    elif operacao in ['-', 'subtração', 'subtracao']:
        resultado = subtracao(num1, num2)
    elif operacao in ['*', 'multiplicação', 'multiplicacao']:
        resultado = multiplicacao(num1, num2)
    elif operacao in ['/', 'divisão', 'divisao']:
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida!"
    return resultado

# Laço que continua até o usuário digitar 'N' ou 'n'
while saida.lower() != 'n':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação que deseja (+, -, *, / ou nome da operação): ')
    
   
    print(f'Resultado da operação: {resultado}')
    
    saida = input('Deseja continuar? (S/N): ')

print('Programa encerrado.')
