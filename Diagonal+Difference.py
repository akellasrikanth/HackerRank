
# coding: utf-8

# In[21]:

#!/bin/python3

import sys


n = int(input().strip())
a = []
diag_1 = 0
diag_2 = 0
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)
for i in range(n):
    diag_1 = diag_1 + a[i][i]
for j in range(0,n,1):
    diag_2 = diag_2 + a[j][n-1-j]
result = diag_1 - diag_2
if result < 0:
    print(result * -1)
else:
    print(result)


# In[ ]:



