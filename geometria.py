import math

# Função de cálculo de área de um retangulo
def calcularAreaRetangulo(base, altura):
    return(base * altura)

# Função de cálculo do perimetro de um retângulo
def calcularPerimetroRetangulo(base, altura):
    return(2 * (base * altura))

# Função de cálculo da área de um circulo
def calcularAreaCirculo(r):
    return(math.pi * math.pow(r, 2))

# Função de cálculo do perímetro de um circulo
def calcularPerimetroCirculo(r):
    return(2 * math.pi * r)