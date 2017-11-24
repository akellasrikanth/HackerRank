
# coding: utf-8

# In[1]:

import json
student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
           "102":{"class":'V', "Name":'David',  "Roll_no":8},
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
print(json.dumps(student));


# In[2]:

import json
student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
           "103":{"class":'V', "Name":'David',  "Roll_no":8},
           "102":{"class":'V', "Name":'Samiya', "Roll_no":12}}
print(json.dumps(student, sort_keys=True));


# In[4]:

import json
tup1 = ('Red', 'Black', 'White');
print(json.dumps(tup1));


# In[7]:

import json
list1 = [5, 12, 13, 14];
print(json.dumps(list1));


# In[8]:

import json
string1 = 'Python and JSON';
print(json.dumps(string1));


# In[12]:

import os
os.popen("Start cmd")


# In[ ]:



