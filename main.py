# Importação das bibliotecas personalizadas.
import matematica
import geometria

# Importação da biblioteca de interface gráfica
import easygui

# Lista de opções do menu
itens = ['Soma', 'Subtração', 'Multiplicação', 'Divisão']

# Entrada de dados do usuário
x = int(easygui.enterbox("Digite um número inteiro", "Entrada de dados"))
y = int(easygui.enterbox("Digite outro número inteiro: ", "Entrada de dados"))

# Seleção das opções do usuário
escolha = easygui.buttonbox("Qual operção deseja realizar?", "Operação Matemática", itens)

# Carrega as operações matemáticas em variaveis
soma = matematica.somar(x, y)
subtracao = matematica.subtrair(x, y)
multiplicacao = matematica.multiplicar(x, y)
divisao = matematica.dividir(x, y)

# Define qual função será chamada
if (escolha == "Soma"):
    easygui.msgbox(f" O resultado é: {soma}" " Resultado a operação matemática")
elif (escolha == "Subtração"):
    easygui.msgbox(f" O resultado é: {subtracao}", " Resultado a operação matemática")
elif (escolha == "Multiplicação"):
    easygui.msgbox(f" O resultado é: {multiplicacao}", " Resultado a operação matemática")
else:
    easygui.msgbox(f" O resultado é: {divisao}", " Resultado a operação matemática")