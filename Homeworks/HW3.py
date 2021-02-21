#!/usr/bin/env python
# coding: utf-8

# In[8]:


firstlist=[]
secondlist=[]
def prime_first(sayi):
    for i in range(2,sayi):
        if sayi%i==0:
            break
    else:
        firstlist.append(sayi)
        
def prime_second(sayi):   
    for i in range(2,sayi):
        if sayi%i==0:
            break
    else:
        secondlist.append(sayi)


# In[10]:


for sayi in range(0,1000):
    #firstlist=[]
    #secondlist=[]
    if sayi!=0 and sayi!=1 and sayi in range(0,500):
        prime_first(sayi)
        if sayi==499:
            print("Prime First: "+str(firstlist))
            firstlist=[]
    elif sayi in range(500,1000):    
        prime_second(sayi)
        if sayi==999:
            print("Prime Second: "+str(secondlist))
            secondlist=[]


# In[ ]:




