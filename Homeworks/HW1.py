#!/usr/bin/env python
# coding: utf-8

# In[103]:


import random as rd
adim=1
list1=[]
list2=[]
list3=[]
AsalSayilar=[list1,list2,list3]
while adim<10:
    sayi=rd.randint(2,100)
    bolen=[]
    for i in range(2,sayi):
        if (sayi % i) == 0:
            bolen.append(i)
            
    if len(bolen)==0 and sayi not in list1 and sayi not in list2 and sayi not in list3:
        if len(list1)<3:
            list1.append(sayi)
        elif len(list2)<3:
            list2.append(sayi)
        else:
            list3.append(sayi)
        adim+=1
print(AsalSayilar)


# In[ ]:




