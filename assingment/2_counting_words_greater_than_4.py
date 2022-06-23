#!/usr/bin/env python
# coding: utf-8

# In[8]:


def add(n):
    f = open("jvm.dat","w")
    for i in range(n):
        f.write(input("Enter Your words : "))
        f.write("\n")
    f.close()
add(4)
def words():
    f = open("jvm.dat","r")
    line = 1
    for i in f:
        word = i.split()
        ctr= 0
        for j in word:
             if len(j) >4:
                ctr+=1
        print("Results in line ",line,"= ",ctr)
        line+=1
words()  


# In[ ]:




