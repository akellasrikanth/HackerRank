
# coding: utf-8

# In[1]:

k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)

print(((sum(myset)*k)-(sum(arr)))//(k-1))


# In[ ]:



