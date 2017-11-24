
# coding: utf-8

# In[11]:

def minimumBribes(q):
    last_index = len(q) - 1
    count = 0
    swaped = False
    comps = 0
    for i, v in enumerate(q):
        if (v - 1) - i > 2:
          #  print(v)
           # print(i)
            return "Too chaotic"
    for i in range(0, last_index):
        for j in range(0, last_index):
            comps += 1
            if q[j] > q[j+1]:
                temp = q[j]
                q[j] = q[j+1]
                q[j+1] = temp
                count += 1
                swaped = True
        
        if swaped == True:
            swaped = False
        else:
            break
    return count

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        q = list(map(int, input().strip().split(' ')))
        result = minimumBribes(q)
        print(result)


# In[ ]:



