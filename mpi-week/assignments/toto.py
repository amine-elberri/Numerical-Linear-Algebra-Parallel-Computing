#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK= COMM.Get_rank()
SIZE = COMM.Get_size()

def f1():
    print("toto",RANK,SIZE)
    
f1()

