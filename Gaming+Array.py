
# coding: utf-8

# In[3]:

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    m = [a[0]]
    for i in range(1, n):
        if a[i] > m[-1]:
            m.append(a[i])
            
    if len(m)%2 != 0:
        return "BOB"
    
    return "ANDY"
    
    
for i in range(int(input())):
    print(solve())
        
    


# In[ ]:



