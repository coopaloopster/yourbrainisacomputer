#!/usr/bin/env python
# coding: utf-8

# In[9]:


threesome=0 
fivesum=0 
fifteensum=0 
totalsum=0

for x in range (0,1000):
    if x % 3 == 0:
        threesome += x
    
for x in range(0,1000):
    if x % 5 == 0:
        fivesum += x
    
for x in range (0,1000): 
    if x % 15 == 0:
        fifteensum += x
    
    
    totalsum = threesome + fivesum - fifteensum    
print(totalsum)    


# In[ ]:




