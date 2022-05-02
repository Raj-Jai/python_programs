#!/usr/bin/env python
# coding: utf-8

# In[16]:


#opening file
f = open("newf.txt","r+")


linelist = f.readlines()
all = []
#Breaking File Into List
for i in range(len(linelist)):
    all.append(linelist[i].split(" "))

# Adding some space between    
for i in range(len(all)):
    for j in range(len(all[i])-1):
        all[i].insert(2*j + 1," ")
        
# Adjusting end line character
for i in range(len(all)):
    all[i][-1] = all[i][-1][:-1]
    all[i].append("\n")        

f.seek(0)
print("Before = ")
print( f.read())


#Input
userin = input("Find & Replace = ")
fnr = userin.split()

#Finding and Replacing words in List

for i in range(len(all)):
    till = int(len(all[i])/2)
    for j in range(till):
        if all[i][j*2].lower() == fnr[0].lower():
            all[i][j*2] = fnr[1]

#Writing updated list in file
f.seek(0)
'''#testing
print(all)'''
for i in range(len(all)):
    f.writelines(all[i])      
f.seek(0)
print("After = ")
print(f.read())
f.close()


# In[ ]:




