import numpy as np 

# def minimosQuadradosV2(numPonts, x, y):
#     h = getVetoresG(numPonts, x)

#     a = []

#     b = []


#     for i in range(2):
#         aux = []
#         secondAux = []
#         for j in range(2):
#             value = 0
#             secondValue = 0
#             for k in range(numPonts):
#                 value += h[i][k] * h[j][k]
#                 secondValue += h[i][k] * y[k]
#             aux.append(value)
#             secondAux.append(secondValue)
#         a.append(aux)
#         b.append(secondValue)

#     print(a)
#     print('\n')
#     print(b)


#     # funcao para resolver sistema linear
#     sistema = np.linalg.solve(a, b)

#     return sistema

def getVetoresG(grau, numPonts, x):
    g = []
    for i in range(grau+1):
        aux = []
        for j in range(numPonts):
            # faz uma potencia do valor no vetor x pelo indice i que roda de acordo com 
            # o grau do meu polinomio
            aux.append(pow(x[j], i))
        g.append(aux)
    print(g)
    return g 

def minimosQuadradosV1(grau, numPonts, x, y):
    h = getVetoresG(grau, numPonts, x)

    a = []

    b = []

    for i in range(grau+1):
        aux = []
        for j in range(grau+1):
            aux.append(np.dot(h[i], h[j]))
        a.append(aux)
        b.append(np.dot(h[i], y))

    print(a)
    print('\n\n')
    print(b)


    # funcao para resolver sistema linear
    sistema = np.linalg.solve(a, b)

    return sistema


def main():
    numPonts = int(input("Digite o numero de entradas que haverá: "))
    grau = int(input("Digite o grau do ajuste: "))

    x = []
    y = []

    for i in range(numPonts):
        x.append(float(input(f"Digite o valor de x - ({i}): ")))
        y.append(float(input(f"Digite o valor de y - ({i}): ")))


    sistema = minimosQuadradosV1(grau, numPonts, x, y)

    for i in range(len(sistema)):
        print(f"ALPHA{i+1} = {round(sistema[i], 2)}")

    valorExtrapolar = float(input("Digite o valor para extrapolar: "))

    valorExtrapolado = 0

    for expoente, coeficiente in enumerate(sistema):
        valorExtrapolado += coeficiente * pow(valorExtrapolar, expoente)

    print(f"O valor extrapolado é: {round(valorExtrapolado, 2)}")

main()