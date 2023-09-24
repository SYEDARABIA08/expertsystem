#!/usr/bin/env python
# coding: utf-8

# In[8]:


print([1, 24, 76])


print(['red', 24, 98.6])


print([ 1, [5, 6], 7])

print([])



# In[10]:


for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')


# In[15]:


friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:', friend)
print('Done!')
z = ['Joseph', 'Glenn', 'Sally']
for x in z:
    print('Happy New Year:', x)
print('Done!')


# In[16]:


greet = 'Hello Bob'
print(len(greet))

x = [ 1, 2, 'joe', 99]
print(len(x))



# In[17]:


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

print(a)


# In[20]:


t = [9, 41, 12, 3, 74, 15]
t[1:3]
t[:4]
t[3:]
t[:]



# In[21]:


stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)

stuff.append('cookie')
print(stuff)


# In[29]:


some = [1, 9, 21, 10, 16]
9 in some

15 in some



# In[30]:


nums = [3, 41, 12, 9, 74, 15]
print(len(nums))
6
print(max(nums))
74
print(min(nums))
3
print(sum(nums))
154
print(sum(nums)/len(nums))
25.6


# In[ ]:


numlist = list()
while True :
 inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
print('Average:', average)


# In[ ]:


abc = 'With three words'
stuff = abc.split()
print(stuff)
['With', 'three', 'words']
print(len(stuff))
3
print(stuff[0])
With


# In[ ]:


words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


# In[ ]:





# In[ ]:





# In[ ]:




