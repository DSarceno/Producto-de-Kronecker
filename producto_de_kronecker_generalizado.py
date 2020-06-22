# Se definen las priemras dos matrices
A = [[1,2,3], [3,2, 1]]                                        # matriz de mxn
B = [[1, 1,1], [1,1,0]]                                        # matriz de pxq
resultado = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]       # matriz de (mp)x(nq)

# Se toma un ciclo que multiplique cada entrada de la matriz A con la matriz B

for i in range(len(A)):
    for j in range(len(A[0])):
        for k in range(len(B)):
            for l in range(len(B[0])):                                                              # Con los ciclos anidados, nos ubicamos en cada una de las entradas de A y las multiplicamos por las entradas de B
                resultado[(len(B)*(i-1))+(k+1)][(len(B[0])*(j-1))+(l+1)] = A[i][j] * B[k][l]             # por definicion, construimos la matriz solucion

# Expresamos el resultado en forma matricial

for i in range(len(resultado)):             
    print(resultado[i])
