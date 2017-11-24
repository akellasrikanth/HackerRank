
# coding: utf-8

# In[16]:

n_A = int(input())
A = input()
set_A_list = A.split(" ")
set_A = set(set_A_list)
no_other_sets = int(input())
for i in range(0,no_other_sets):
    operation = input()
    operation_list = operation.split(" ")
    B = input()
    set_B_list = B.split(" ")
    set_B = set(set_B_list)
    if operation_list[0] == "intersection_update":
        set_A.intersection_update(set_B)
    elif operation_list[0] == "update":
        set_A.update(set_B)
    elif operation_list[0] == "symmetric_difference_update":
        set_A.symmetric_difference_update(set_B)
    elif operation_list[0] == "difference_update":
        set_A.difference_update(set_B)
print(set_A)
set_a = set()
for i in set_A:
    a = int(i)
    set_a.add(a)
print(set_a)
print(sum(set_a))


# In[ ]:



