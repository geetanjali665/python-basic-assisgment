#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""1.What are the two values of the Boolean data type? How do you write them?
True
False


"""


# In[2]:


"""2. What are the three different types of Boolean operators?
1. AND
2. OR
3. NOT

"""


# In[3]:


(5 > 4) and (3 == 5)


# In[4]:


not (5 > 4)


# In[5]:


(5 > 4) or (3 == 5)


# In[6]:


not ((5 > 4) or (3 == 5))


# In[7]:


(True and True) and (True == False)


# In[8]:


(not False) or (not True)


# In[9]:


""" 5. What are the six comparison operators?
1 . >
2. <
3. >=
4.<=
5. ==
6. !=





"""


# In[10]:


""" How do you tell the difference between the equal to and assignment operators?Describe a
condition and when you would use one.


assigm,ent operator is used when we have to assign some value on variables and euals to is used when we have to make some
comparision.

a = 10 (it is assignment)
a ==10 (it is comaprision opertaor)


"""


# In[11]:


"""Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam."""


# In[15]:


spam = int(input("Enter the value of spam: "))
if spam == 1:
    print("Hello")
elif spam ==2:
    print("Howdy")
else:
    print("Greetings!")

    
    


# In[ ]:


"""9.If your programme is stuck in an endless loop, what keys you’ll press?
Ctrl+c
"""


# In[ ]:


"""  10. How can you tell the difference between break and continue?
continue : when you give continue statement then after the continue statement no programm will excute and curshor will shift to
loop.

Break : when we got break statement in loop then then the cursor will automatically comes out form loop.

"""


# In[ ]:


"""In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
both three are same statement 

"""


# In[ ]:


""" Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop."""


# In[13]:


for i in range(10):
    print(i+1)


# In[14]:


i = 0
while i in range(10):
    print(i+1)
    i = i+1


# In[16]:


""" 13. If you had a function named bacon() inside a module named spam, how would you call it after
importing spam?

from span import bacon

"""


# In[ ]:




