# Se definen las priemras dos matrices
A = [[1, 2], [2, 1]]
B = [[1, 1], [1,0]]
resultado = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
# Se toma un ciclo que multiplique cada entrada de la matriz A con la matriz B

for i in range(2):
    for j in range(2):
        for k in range(2):
            for l in range(2):                                                              # Con los ciclos anidados, nos ubicamos en cada una de las entradas de A y las multiplicamos por las entradas de B
                resultado[(2*(i-1))+(k+1)][(2*(j-1))+(l+1)] = A[i][j] * B[k][l]             # por definicion, construimos la matriz solucion

for i in range(len(resultado)):             # para expresarlo en forma matricial
    print(resultado[i])







