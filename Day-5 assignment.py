#!/usr/bin/env python
# coding: utf-8

# In[2]:


list1=[1,2,3,4,5,6,6,765,34,4,5]
list2=[]
for each in list1:
    if each%3==0:
        list2.append(each)
print(list2)        
    


# In[9]:


list1=[1,2,3,4,5,6,6,765,34,4,5]
list1.sort(reverse= 1)


# In[10]:


list1


# In[14]:


list2=[('a',2),('b',56),('c',76),('d',334),('e',4)]
print (list2)


# In[17]:


def fun1(x):
    print(x)
    return x [1]
list2.sort(key=fun1)    


# In[20]:


value=[0,1,2,10,4,1,0,56,2,0,1,3,0,0,56,4]
value.sort()
print (value)


# In[21]:


value


# In[36]:


def mergesortedArrays(arr1,arr2):
    i=0
    j=0
    len1 = len(arr1)
    len2 = len(arr2)
    arr = []
    while ((i<len1) and (j<len2)):
        if (arr1[i]<arr2[j]):
            arr.append(arr1[i])
            i= i + 1
        else:
            arr.append(arr2[j])
            j= j + 1
    while(i<len1):
        arr.append(arr1[i])
        i= i + 1
        
    while(j<len2):
        arr.append(arr2[j])
        j= j + 1
        return arr
arr2 = [10,20,40,60,70,80]
arr1 = [5,15,25,35,45,60]
arr = mergesortedArrays(arr1,arr2)
print(arr)


# In[ ]:




