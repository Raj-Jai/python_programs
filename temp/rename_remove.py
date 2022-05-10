import os
def copy():
    f1 = open("story.txt","r")
    f2 = open("open.txt","w")
    str = f1.read()
    for i in str :
        if i in ["A","E","I","O","U"]:
            continue
        f2.write(i)
    f1.close()
    f2.close()
    os.remove("story.txt")
    os.rename("open.txt","story.txt")
copy()
