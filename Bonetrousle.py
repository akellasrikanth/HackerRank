
# coding: utf-8

# In[1]:

for _ in range(int(input())):
    a,b,c = map(int,input().split())
    MinSum = c*(c+1)//2
    MaxSum = c*(2*(b-c+1)+(c-1))//2
    array = [i for i in range(1,c+1)]
    if a >= MinSum and a <= MaxSum:
        add = (a-MinSum)//c
        array1 = [i+add for i in array]
        remainder = (a-MinSum)%c
        for j in range(len(array1)-1,len(array1)-1-remainder,-1):
            array1[j] += 1
        for i in array1:
            print(i,end=" ")
        print("")
    else:
        print ("-1")


# In[ ]:

4
12 8 3
10 3 3
9 10 2
9 10 2

