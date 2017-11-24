
# coding: utf-8

# In[2]:

#!/bin/python3

import sys

def timeConversion(s):
    # Complete this function
    tm = s[8:10]
    hr = int(s[0:2])
    mn = s[3:5]
    sc = s[6:8]
    if tm == "PM":
        if hr == 12:
            print("{}:{}:{}".format(hr,mn,sc))
        else:
            hr = int(s[0:2]) + 12
            print("{}:{}:{}".format(hr,mn,sc))
    elif tm == "AM":
        if hr == 12:
            hr = '00'
            print("{}:{}:{}".format(hr,mn,sc))
        elif hr < 12:
            hr = s[0:2]
            print("{}:{}:{}".format(hr,mn,sc))
        
        
s = input().strip()
timeConversion(s)


# In[ ]:



