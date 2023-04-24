#Exercise 6: Pi calculation

#Question 1 :

N = 840

def compute_pi(N):
    sum = 0
    for i in range(1,N):
        sum += 1/(1+((i-0.5)/N)**2)
    return (4/N)*sum

print('Value of pi : {} from processor {} '.format(compute_pi(N),RANK))

#Question 2:

if RANK ==0:
    sum = 0
    for i in range(1,420-1):
        sum += 1/(1+((i-0.5)/N)**2)
    print('the partial sum by process 0 is : ',(4/N)*sum)
    COMM.send((4/N) *sum,dest = 1)
if RANK == 1:
    recv = COMM.recv(source = 0)
    for i in range(420,840):
        recv += (4/N)* 1/(1+((i-0.5)/N)**2)
    print('the sum of the two results is ')
    print('The value of pi : ',recv)

#Part 2
import numpy as np
N = 8400 # Increasing the value of N generally increases the execution time
start_time = MPI.Wtime()

local_n = int(N / SIZE)
local_sum = 0.0
for i in range(RANK * local_n + 1, (RANK + 1) * local_n + 1):
    x = (i - 0.5) / N
    local_sum += 4.0 / (1.0 + x**2)

partial_sums = COMM.gather(local_sum, root=0)

if RANK == 0:
    pi = np.sum(partial_sums) / N
    end_time = MPI.Wtime()
    print("Approximate value of pi:", pi)
    print("Execution time:", end_time - start_time)
else:
    COMM.send(local_sum, dest=0)

if RANK == 0:
    for i, partial_sum in enumerate(partial_sums):
        print("Partial sum for rank", i, ":",partial_sum)
