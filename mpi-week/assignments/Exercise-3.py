# Exercise 3 : Sending in a ring

if RANK == 0:
    data = int(input('Entrer unevaleur: '))
else :
    data = None

for i in range(SIZE):
    if RANK == i:
        data = data + RANK
        print('Le processeur {} a {}'.format(RANK,data))
        next_rank = RANK + 1
        COMM.send(data , dest = next_rank)
    else :
        prev_rank = RANK -1

    data = COMM.recv(source = prev_rank)
