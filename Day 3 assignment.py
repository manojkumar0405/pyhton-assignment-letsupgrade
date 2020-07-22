#!/usr/bin/env python
# coding: utf-8

# In[4]:


num=int(input("enter any number: "))
total=0
value=1
while(value<=num):
    total=total+value
    value=value+1
print("sum of number from 1 to {0}={1}".format(num,total))    


# In[13]:


num=eval(input("enter a number:"))
if num>1:
    for i in range (2,num):
        if(num%i)==0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
else:
                print (num,"is not a prime number")


# In[14]:


sum1=0
for each in range(1,11):
    print(each)


# In[ ]:




