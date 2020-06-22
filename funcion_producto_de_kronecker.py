# En este programa se define una funcion que realize el producto de kronecker para dos matrices arbitrarias

# 20.06.2020
# Diego Sarceño



# 1. Se define la funcion del producto de kronecker
def pKronecker(m,n,p,q,M_1,M_2):
    '''
    Esta funcion para crear la matriz del producto de kronecker

    Argumentos:
        m y p son las filas de ambas matrices       tipo int
        n y q son las columnas de la matriz         tipo int
        Matriz_1 y Matriz_2 son las matrices para realizar el producto          tipo list

    Devuelve una matriz de (mp)x(nq) con entradas acorde a la definición del producto       tipo list
    '''
    # 1.1. Se corrobora que las matrices tengan sublistas de la misma longitud
    for i in range(m-1):
        if len(M_1[i]) != len(M_1[i+1]):
            print('No es una matriz, no todas las filas tienen la misma longitud.')
            return
    
    for i in range(p-1):
        if len(M_2[i]) != len(M_2[i+1]):
            print('No es una matriz, no todas las filas tienen la misma longitud.')
            return
    # 1.2. Se define la matriz en la cual se ingresarán los datos del producto
    Matriz_Resultado = [[0]*(n * q)]*(m * p) # Matriz de (mp)x(nq)
    print(Matriz_Resultado)

    # 1.3. Se multiplican los terminos y se añaden a la matriz resultado
    for i in range(0,m):                        # fila matriz 1
        for j in range(0,n):                    # columna matriz 1
            for k in range(0,p):                # fila matriz 2
                for l in range(0,q):            # columna matriz 2
                    alpha = (p*i) +k
                    beta = (q*j) +l
                    Matriz_Resultado[alpha][beta] = M_1[i][j]*M_2[k][l]
                    '''
                    Con la siguiente linea comprobamos que nos estamos refiriendo a la entrada correcta
                    en la matriz resultado
                    '''
                    print(alpha, beta)       
    # 1.4. Se imprime la lista en forma matricial
    for i in range(len(Matriz_Resultado)):
        print(Matriz_Resultado[i])
    return

# 2. Se definen las matrices        EL USUARIO SOLO INGRESA LAS MATRICES
Matriz_1 = [[1,1],[1,1]] # Matriz de mxn
Matriz_2 = [[1,0],[0,1]] # Matriz de pxq  

    # 2.1. Se definen las dimensiones de las matrices
m = len(Matriz_1)
n = len(Matriz_1[0])
p = len(Matriz_2)
q = len(Matriz_2[0])


# 3. Se valúa la función
pKronecker(n=n,m=m,p=p,q=q,M_1=Matriz_1, M_2=Matriz_2)


