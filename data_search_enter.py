#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Functions
def data_enter():
    f = open("details.txt","a")
    n = int(input("NUMBER OF CONTACTS: "))
    for i in range(n):
        name = input("Name: ")
        roll = input("Roll No: ")
        mail = input("E-mail : ")
        f.write( "\n" + name + " " + roll + " " + mail)
    f.close()
    
def data_search():
     f = open("details.txt","r")
     sname = input("Name to search")
     str =" "
     while True:
        str = f.readline()
        if str =="":
            break
        lis = str.split()
        if sname.lower() == lis[0].lower() :
            print("Name:",lis[0],"\nRoll: ",lis[1],"\nE-mail",lis[2],"\n")
     f.close()


#Program start

print("Chose your option:\n 1)Enter the data(e)\n 2)Search data(s)")
opt = input()

# Data Entering

if opt.lower() == "e":
    data_enter()


# Data Searching
    
elif opt.lower() == "s":
    data_search()
   


# In[ ]:




