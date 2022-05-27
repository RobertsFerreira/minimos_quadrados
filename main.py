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

def pause():
    input("Pressione enter para continuar...")
    exit(0)

def getVetoresG(grau, numPonts, x):
    g = []
    for i in range(grau+1):
        aux = []
        for j in range(numPonts):
            # faz uma potencia do valor no vetor x pelo indice i que roda de acordo com 
            # o grau do meu polinomio
            aux.append(pow(x[j], i))
        g.append(aux)
    
    print("\n")

    for i in range(len(g)):
        print(f'G{i+1}: {g[i]}')

    return g 

def minimosQuadradosV1(grau, numPonts, x, y):
    h = getVetoresG(grau, numPonts, x)

    matrizCoeficientes = []

    termosIndependente = []

    for i in range(grau+1):
        aux = []
        for j in range(grau+1):
            aux.append(np.dot(h[i], h[j]))
        matrizCoeficientes.append(aux)
        termosIndependente.append(np.dot(h[i], y))

    # funcao para resolver sistema linear
    sistema = np.linalg.solve(matrizCoeficientes, termosIndependente)
    
    print("\n")

    _sistema = []

    print("SISTEMA:")

    for i in range(len(matrizCoeficientes)):
        _sistema.append(matrizCoeficientes[i])
    
    for i in range(len(_sistema)):
        _sistema[i].append(termosIndependente[i])

    for l in range(len(_sistema)):
        for c in range(len(_sistema[l])):
            print(f'[{_sistema[l][c]}]', end='')
        print()

    print()
    
    return sistema


def main():
    numPonts = int(input("Digite o numero de entradas que haverá: "))
    if numPonts <= 5:
        grau = int(input("Digite o grau do ajuste (1 - Reta Linear | 2 - Parabola): "))

        if grau < 1 or grau > 2:
            print("Grau inválido\n\n\n")
            main()
        else:
            x = []
            y = []

            for i in range(numPonts):
                x.append(float(input(f"Digite o valor de x - ({i}): ").replace(',', '.')))
                y.append(float(input(f"Digite o valor de y - ({i}): ").replace(',', '.')))


            sistema = minimosQuadradosV1(grau, numPonts, x, y)

            for i in range(len(sistema)):
                print(f"ALPHA{i+1} = {round(sistema[i], 2)}")
            
            _sistema = []
            
            for i in range(len(sistema)):
                _sistema.append(sistema[i])
            
            print("\n")

            _sistema.reverse()

            formula = "Y = "

            for expoente, valor in enumerate(_sistema):
                formula += f"{round(valor, 2)}"
                if expoente != len(_sistema) - 1:
                    formula += f"x elevado a {(len(_sistema) - 1) - expoente}"
                if expoente != len(_sistema)-1:
                    formula += " + "

            print(f"Formula: {formula}")

            print("\n")

            valorDigitado = input("Digite o valor para extrapolar: ")

            valorExtrapolar = float(0 if valorDigitado == '' else valorDigitado.replace(',', '.'))

            valorExtrapolado = 0

            for expoente, coeficiente in enumerate(sistema):
                valorExtrapolado += coeficiente * pow(valorExtrapolar, expoente)

            print("\n")
            
            print(f"O valor extrapolado é: {round(valorExtrapolado, 2)}")

            print("\n")
    else:
        print("O numero de pontos deve ser menor que 5\n\n\n")
        main()

    pause()

main()