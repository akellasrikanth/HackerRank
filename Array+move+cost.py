
# coding: utf-8

# In[ ]:




# In[ ]:




# In[204]:

def sum_array(num):
    new_list = []
    cost = []
    total_cost = 0
    while(len(num) != 1):
        add = num[0] + num[1]
        num.append(add)
        new_list.append(num[0])
        new_list.append(num[1])
        num.remove(num[1])
        num.remove(num[0])
        cost.append(add)
        num.sort()
    for i in range(len(cost)):
        total_cost = total_cost +  cost[i]
    return total_cost


# In[211]:

print(sum_array([1,2,3,4]))


# In[ ]:



