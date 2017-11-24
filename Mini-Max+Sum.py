
# coding: utf-8

# In[5]:

#!/bin/python3

import sys
sum_list = list()
arr = list(map(int, input().strip().split(' ')))
for i in range(0,len(arr)):
    sum = 0
    for j in range(0,len(arr)):
        sum = sum + arr[j]
    sum = sum - arr[i]
    sum_list.append(sum)
min_val = min(sum_list)
max_val = max(sum_list)
print("{} {}".format(min_val,max_val))


# In[ ]:



