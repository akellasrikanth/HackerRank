
# coding: utf-8

# In[ ]:

eng = int(input())
eng_roll = input()
eng_roll_list = eng_roll.split(" ")
fren = int(input())
fren_roll = input()
fren_roll_list = fren_roll.split(" ")
set_eng = set(eng_roll_list)
set_fren = set(fren_roll_list)
result = set_eng.intersection(set_fren)
length = len(result)
print(length)

