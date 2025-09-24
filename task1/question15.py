#Rotate an n*n matrix by 90° clockwise.Take a user input for a matrix and print the elements in spiral order

def rotation(matA):
    print(matA)
    mat_transposed=[]
    for i in range(order):
        mat_element=[]
        for j in range(order):
            mat_element.append(matA[j][i])
        mat_transposed.append(mat_element)
    print(mat_transposed)
    for i in range(order):
        mat_transposed[i].reverse()
    return mat_transposed

def readmat(order):
    print("Enter elements: \n")
    matA=[]
    for i in range(order):
        mat_elements=[]
        for j in range(order):
            mat_elements.append(int(input()))
        matA.append(mat_elements)
    return matA

def printspiral(mat):
    for i in range(order):
        for j in range(i):
            print(mat[i][j])
global order
order=int(input("Enter order: "))
print(rotation(readmat(order)))