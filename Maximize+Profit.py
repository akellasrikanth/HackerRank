
# coding: utf-8

# In[1]:

#!/bin/python3

import sys

def maximizeProfit(a, b, m, k):
    # Complete this function
    max_val = m * k
    for i in range(len(a)):
        rev = a[i] * b[i] * m
        if rev > max_val:
            max_val = rev
    return max_val

if __name__ == "__main__":
    n, m, k = input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    result = maximizeProfit(a, b, m, k)
    print(result)


# ## Sample Input
# 
# 10 1 1000
# 1 2 3 4 5 6 7 8 9 10
# 10 9 8 7 6 5 3 2 1 1

# ## Sample Output
# 
# 1000

# ## Sample Input
# 
# 5 10 3
# 2 3 4 1 5
# 1 3 2 4 5

# ## Sample Output
# 
# 250
