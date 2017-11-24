
# coding: utf-8

# In[50]:

#!/bin/python3        #Correct code

import sys
import re

def allUnique(x):
    seen = set()
    return not any(i in seen or seen.add(i) for i in x)

if __name__ == "__main__":
    n = int(input().strip())
    dict_1 = dict()
    list_unique_name = list()
    list_unique_value = list()
    if 1 <= n <= 10**5:
        for a0 in range(n):
            name, value = input().strip().split(' ')
            name, value = [str(name), int(value)]
            count1 = 0
            count2 = 0
            count3 = 0
            if 1 <= len(name) <= 10:
                if re.match(r'^[a-zA-Z]+\Z', name) is not None:
                    if 1<= value <= 10**9:
                        list_unique_name.append(name)
                        list_unique_value.append(value)
                        list_new = [int(d) for d in str(value)]
                        for ele in list_new:
                            if ele == 4:
                                count1 = count1 + 1     
                            if ele == 7:
                                count2 = count2 + 1 
                            if ele == 1 or ele == 2 or ele == 3 or ele == 5 or ele == 6 or ele == 8 or ele == 9 or ele == 0:
                                count3 = count3 + 1
                        if count3 == 0:
                            if count1 > 0 and count2 > 0:  
                                dict_1[value] = name     
             #   if count3 == 0:
                    #if count1 > 0 and count2 > 0:  
                        #dict_1[value] = name         
       # print(dict_1)
        list_1 = []        
        for k,v in dict_1.items():
            list_1.append(k)    
        if any(dict_1) == True:
            name_unique = allUnique(list_unique_name) 
            value_unique = allUnique(list_unique_value)
            if name_unique == True:
                if value_unique == True:    
                    min_no = min(list_1)
                    print(dict_1[min_no])
                else:
                    print("-1")
            else:
                print("-1")
        else:
            print("-1")
    else:
        print("-1")


# In[ ]:

def allUnique(x):
    seen = list()
    return not any(i in seen or seen.append(i) for i in x)


# In[ ]:

4
Hackerbooooooooooooooooook 47
Bestbook 47
కరల్ి 47
Bestbook 4747


# In[47]:

allUnique(['Bestbook','Bestbook'])


# In[ ]:




# In[ ]:



