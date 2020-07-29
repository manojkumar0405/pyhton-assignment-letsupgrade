#!/usr/bin/env python
# coding: utf-8

# In[7]:


n = int(input())
if n%2==1:
    print("weird")
elif n%2==0 and 2<=n<=5:
    print("not weird")
elif n%2==0 and 6<=n<=20:
    print("weird")
else:
    print("not weird")


# In[15]:


def is_leap(i):
    
if i/400 == 0:
    return True
if i/100 == 0:
    return False
if i/4 == 0:
    return True
year=int(input())
print(is_leap())
    


# In[18]:


def is_leap(n):
    leap = False
    
    # Write your logic here
    if n/400 == 0:
        return True
    if n/100 == 0:
        return False
    if n/4 == 0:
        return True
    return leap

year = int(input())
print(is_leap(year))


# In[ ]:




