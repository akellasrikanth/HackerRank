
# coding: utf-8

# In[13]:

size_of_array,num = map(int,input().split())
array = list(map(int,input().split()))
l = []
for i in range(0,size_of_array):
    if array[i] == num:
        l.append(i+1)
if any(l):
    print(max(l))
else:
    print("-1")


# In[ ]:



