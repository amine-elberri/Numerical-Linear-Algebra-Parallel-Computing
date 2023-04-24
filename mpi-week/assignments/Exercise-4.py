# Exercise 4 : Scattering matrix
import numpy as np

m = 8
n = 8 

if RANK ==0:
    A = np.random.randint(10,size=(n,m))
else :
    A = np.zeros((m,n))
    
A_rank1 = []
for i in range(3):
    for j in range(4,7):
        A_rank1.append(A[i,j])

A_rank2 = []
for i in range(4 , 7):
    for j in range(7):
        A_rank2.append(A[i,j])

        
A_rank3 = []
for i in range(4,7):
    for j in range(4,7):
        A_rank3.append(A[i,j])

sendbuff = [A,A_rank1,A_rank2,A_rank3]
recvbuf = COMM.scatter(sendbuff, root = 0)

print('process ',RANK, 'recieved ',recvbuf)
