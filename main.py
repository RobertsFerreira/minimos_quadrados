import numpy as np 

def getVetoresG(numPonts, x):
    g = []
    for i in range(2):
        aux = []
        for j in range(numPonts):
            # faz uma potencia do valor no vetor x pelo indice i que roda de acordo com 
            # o grau do meu polinomio
            aux.append(pow(x[j], i))
        g.append(aux)
    print(g)
    return g 

def minimosQuadradosV2(numPonts, x, y):
    h = getVetoresG(numPonts, x)

    a = []

    b = []


    for i in range(2):
        aux = []
        secondAux = []
        for j in range(2):
            value = 0
            secondValue = 0
            for k in range(numPonts):
                value += h[i][k] * h[j][k]
                secondValue += h[i][k] * y[k]
            aux.append(value)
            secondAux.append(secondValue)
        a.append(aux)
        b.append(secondValue)

    print(a)
    print('\n')
    print(b)


    # funcao para resolver sistema linear
    sistema = np.linalg.solve(a, b)

    return sistema

def minimosQuadradosV1(numPonts, x, y):
    h = getVetoresG(numPonts, x)

    a = []

    b = []

    for i in range(2):
        aux = []
        for j in range(2):
            aux.append(np.dot(h[i], h[j]))
        a.append(aux)
        b.append(np.dot(h[i], y))

    print(a)
    print('\n')
    print(b)


    # funcao para resolver sistema linear
    sistema = np.linalg.solve(a, b)

    return sistema


def main():
    numPonts = int(input("Digite o numero de entradas que haverá: "))

    x = []
    y = []

    for i in range(numPonts):
        x.append(float(input(f"Digite o valor de x({i}): ")))
        y.append(float(input(f"Digite o valor de y({i}): ")))


    sistema = minimosQuadradosV1(numPonts, x, y)

    for i in range(len(sistema)):
        print(f"a{i} = {sistema[i]}")

    sistema2 = minimosQuadradosV2(numPonts, x, y)

    for i in range(len(sistema2)):
        print(f"V2 Teste\n  a{i} = {sistema2[i]}")

main()