# Função de soma
def somar(x, y):
    return (x + y)

# Função de subtração
def subtrair(x, y):
    return (x - y)

# Função de Multiplicação
def multiplicar(x, y):
    return (x * y)

# Função de divisão
def dividir(x, y):

    # Faz a tentativa da divisão
    try:
        return (x / y)
    
    # Tratamento de exceção.
    except ZeroDivisionError:
        return("Não é possivel divisão por zero!!!")