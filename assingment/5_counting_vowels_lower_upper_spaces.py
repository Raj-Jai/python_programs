#!/usr/bin/env python
# coding: utf-8

# In[5]:


def add(n):
    f = open("jvm.dat","w")
    for i in range(n):
        f.write(input("Enter Your words : "))
       
    f.close()
add(4)
def count():
    f = open("jvm.dat","r")
    fcon = f.read()
    vowelc,spacec,lowerc,upperc = 0 ,0 ,0, 0
    for i in fcon:
        if i.lower() in ["a","e","i","o","u"]:
            vowelc+=1
        elif i.isspace():
            spacec+=1
        if i.islower():
            lowerc += 1
        elif i.isupper():
            upperc +=1
    print("vowel",vowelc)
    print("space",spacec)
    print("lower",lowerc)
    print("upper",upperc)
    f.close()
count()
        


# In[ ]:




