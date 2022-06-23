#!/usr/bin/env python
# coding: utf-8

# In[17]:


def add(n):
    f = open("jvm.dat","w")
    for i in range(n):
        f.write(input("Enter Your words : "))
        f.write("\n")
    f.close()
def display():
    f = open("jvm.dat","r")
    ctr = 0
    for i in f:
        if i[0].lower() in ["a","e","i","o","u"]:
            ctr+=1
            print(i ,end="")
    print("vowels enchoumter ",ctr)
    f.close()
add(4)
display()


# In[ ]:




