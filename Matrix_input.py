r1=int(input("enter num of rows for Matrix1: "))
c1=int(input("enter num of columns for Matrix1: "))

r2=int(input("enter num of rows for matrix2: "))
c2=int(input("enter num of columns for matrix2: "))

if(c1==r2):
    print("enter elements for MAtrixA")
    A=[]
    for i in range(r1):
        row=list(map(int,input(f"Row {i+1}:").split()))
        A.append(row)

    print("enter elements for  MatrixB")
    B=[]
    for i in range(r2):
        row=list(map(int,input(f"Row {i+1}:").split()))
        B.append(row)

    C=[]
    for i in range(r1):
        row=[]
        for j in range(c2):
            row.append(0)
        C.append(row)

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                C[i][j]+= A[i][k]*B[k][j]

    print("Resultant Matrix")
    for r in C:
        print(r)
else:
    print("not possible")
