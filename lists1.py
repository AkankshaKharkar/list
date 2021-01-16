#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[12,-7,5,64,-14]
output1=[]
list2=[12,14,-95,3]
output2=[]
for i in list1:
    if i>0:
        output1.append(i)
for j in list2:
    if j>0:
        output2.append(j)
print("Input:list1=",list1)
print("Output:",output1)
print("Input:list2=",list2)
print("Output:",output2)

