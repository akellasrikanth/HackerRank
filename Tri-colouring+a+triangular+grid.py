
# coding: utf-8

# In[1]:

n ,c = map(int,input().split())
if n >= 1 and c >= 1:
    if n + c <= 14:
        a = c*(c-1)**((n**2)-1)
        b = (10**9) + 7
        c = a % b
        d = c % b
        print(c)
    while a <= 10:
        a = a % b
print(a)


# In[ ]:

n ,c = map(int,input().split())
if n >= 1 and c >= 1:
    if n + c <= 14:
        a = c*(c-1)**((n**2)-1)
        b = (10**9) + 7
    while a <= 10:
        a = a % b
print(a)


# In[ ]:




# In[2]:

n ,c = map(int,input().split())
if n >= 1 and c >= 1:
    if n + c <= 14:
        if c == 3:
            a = c*(c-1)**((n**2)-1)
            b = (10**9) + 7
            print(a % b)
        elif c == 2:
            d = (n**2) // 2
            a = (c**(d+1)) * ((c-1) ** d)
            print(a)


# In[4]:

a = 9 // 2
print(a)


# In[ ]:



