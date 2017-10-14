import sys
def Matrix_chain_multiplication(x, y):
    matrice = [[0 for x in range(y)] for x in range(y)]
    for i in range(1, y):
        matrice[i][i] = 0
    for z in range(2, y):
        for i in range(1, y-z+1):
            j = i+z-1
            matrice[i][j] = sys.maxint
            for k in range(i, j):
                q = matrice[i][k] + matrice[k+1][j] + x[i-1]*x[k]*x[j]
                if q < matrice[i][j]:
                    matrice[i][j] = q
    return matrice[1][y-1]
array = list()
num = raw_input("Enter how many elements you want:")
print 'Enter numbers in array: '
for i in range(int(num)):
    n = raw_input("num :")
    array.append(int(n))
length = len(array)
print("result =" +str(Matrix_chain_multiplication(array, length)))
