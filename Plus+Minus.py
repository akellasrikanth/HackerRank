
# coding: utf-8

# In[1]:

#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
pos = 0
neg = 0
zer = 0
for ele in arr:
    if ele > 0:
        pos += 1
    elif ele < 0:
        neg += 1
    elif ele == 0:
        zer += 1
res_pos = pos / n
res_neg = neg / n
res_zer = zer / n
print(res_pos)
print(res_neg)
print(res_zer)


# In[ ]:



