#!/usr/bin/env python
# coding: utf-8

# In[12]:


def add(n):
    f = open("jvm.dat","w")
    for i in range(n):
        f.write(input("Enter Your words : "))
        f.write("\n")
    f.close()
add(4)
def display():
    f = open("jvm.dat","r+")
    for i in f:
        word = i.split()
        for j in word:
            print(j+"#",end="")
display()  


# In[ ]:




