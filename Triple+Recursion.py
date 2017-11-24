
# coding: utf-8

# In[2]:

#!/bin/python3

import sys

def tripleRecursion(n, m, k):
    matrix = [[None for i in range(n)] for j in range(n)]
    d = 0
    while(d<n):
        if d == 0:
            matrix[d][d] = m
        else:
            matrix[d][d] = matrix[d-1][d-1] + k
        for i in range(d+1,n):
            matrix[d][i] = matrix[d][i-1]-1
            matrix[i][d] = matrix[i-1][d]-1
        d += 1
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    tripleRecursion(n, m, k)


# In[ ]:



