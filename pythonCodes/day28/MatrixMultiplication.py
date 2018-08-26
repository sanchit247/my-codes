a = [[1,2],[3,4],[5,6]]
b = [[1,3,5],[2,4,6]]
c = [[0 for i in range(len(b[0]))] for j in range(len(a))]

if(len(a) == len(b[0])):
    print("Matrix multiplication is : ")
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                c[i][j] =c[i][j] + a[i][k]*b[k][j]

    for i in c:
        for j in i:
            print(j,end = " ")
        print()
else:
    print("Matrix multiplication not possible")
