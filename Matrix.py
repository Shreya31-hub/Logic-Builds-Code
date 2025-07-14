A=[[1,2,3],
   [4,5,6]]
B=[[5,3,5],
   [5,2,5]]
C=[[0,0,0],
   [0,0,0]]
for i in range(len(A)):
    for j in range(len(B)):
        for k in range(len(C)):
            C[i][j]+= A[i][k]*B[k][j]

for r in C:
    print(r)
