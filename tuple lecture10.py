#!/usr/bin/env python
# coding: utf-8

# In[7]:


x = ('Glenn','Sally','Joseph')
print(x[2])

y = ( 1, 9, 2)	
print(y)		
		
print(max(y))

for iter in y:
    print(iter)


# In[9]:


(x, y) = (4, 'fred')
print(y) 
(a, b) = (99, 98)
print(a) 


# In[15]:


(0, 1, 2) < (5, 1, 2)

(0, 1, 2) < (0, 3, 4)


( 'Jones',	'Sally'	) < ('Jones',	'Sam')


( 'Jones',	'Sally')	> ('Adams',	'Sam')
		



# In[19]:


d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
t
[('a', 10), ('b', 1), ('c', 22)]
for k, v in sorted(d.items()):
    print(k, v)


# In[ ]:




