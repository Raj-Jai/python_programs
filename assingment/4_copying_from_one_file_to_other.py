#!/usr/bin/env python
# coding: utf-8

# In[2]:


def add(n):
    f = open("jvm.dat","w")
    for i in range(n):
        f.write(input("Enter Your words : "))
        f.write("\n")
    f.close()
add(4)
def display():
    f = open("jvm.dat","r+")
    fc = open("copy.txt","w")
    for i in f:
        if "a" in i :
            fc.write(i)
    f.close()
    fc.close()
    fc = open("copy.txt","r")
    print(fc.read())
display()  


# In[ ]:




