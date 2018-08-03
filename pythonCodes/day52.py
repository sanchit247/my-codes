   #Write a program to return Matrix Transpose.
    a =[[1,2,3],[4,5,6],[7,8,9]]

    b =[[0,0,0],[0,0,0],[0,0,0]]

    for i in range(0,3):
        for j in range(0,3):
            b[i][j]=a[j][i]
    print("mattrix is : \n")
    for i in range(len(a)):
        print(a[i])

    print("transpose of matrix is :")
    for i in range(len(a)):
        print(b[i])
