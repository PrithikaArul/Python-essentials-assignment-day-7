#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Program to swap keys and values in a dictionary:
port1={21:"FTP",22:"SSH",23:"telnet",80:"http"}
port2=dict([(value,key) for key,value in port1.items()])
print("Port2 is:",port2)


# In[23]:


#Program to make a new list which contains the sum of the number of tuples:
list1=[(1,2),(3,4),(5,6),(4,5)]
print("The new list is:",sum)
for i,j in list1:
    sum=i+j
    print(sum)


# In[29]:


#Program to make a number of lists in one list into a new list:
list2=[(1,2,3),[1,2],['a','hit','less']]
result=[]
for x,y,z in list2:
    result.append(x)
print(result)

