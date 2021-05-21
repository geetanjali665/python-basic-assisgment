#!/usr/bin/env python
# coding: utf-8

# 
#  1. What exactly is []?
#     
#     it is bascially notation of list.

# 2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)

# In[ ]:


spam = [2,4,6,8,10]

  spam[3] = "hello"


# Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.

# 3. What is the value of spam[int(int('3' * 2) / 11)]?
#    
#     d

# 4. What is the value of spam[-1]?
#   
#      d

# 5. What is the value of spam[:2]?
#     
#      'a ', 'b'

# Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.
# 
# 

# 6. What is the value of bacon.index('cat')?
# 
#   1, 3

# 7. How does bacon.append(99) change the look of the list value in bacon?
# 
#     bacon.append(99) add the value 99 in the last of the list. and the new list become  [3.14, 'cat,' 11, 'cat,' True, 99] 
# 

# 8. How does bacon.remove('cat') change the look of the list in bacon?
#    
#    it remove the cat from the bacon list and the new list become  [3.14, 'cat', 11, True]

# In[ ]:


bacon =  [3.14, 'cat', 11, 'cat', True]
bacon.remove('cat')


# In[12]:


bacon


# 9. What are the list concatenation and list replication operators?
# 
#    a = [1, 2, 3], b = [4, 5, 6] 
#     
#     list concatentation is a+b
#     and list replication is a*3
# 

# 10. What is difference between the list methods append() and insert()?
#   
#     list append method add any value to the last index of the list and list insert add any value at any required index.
# 
# 

# 11. What are the two methods for removing items from a list?
#   
#     pop and remove commands are use for removing items from the list
# 
# 

# 12. Describe how list values and string values are identical.
#     
#     string and list values both are iterable
#   

# 13. What's the difference between tuples and lists?
#   
#     lists are mutable and tuples are immutable.
# 

# 14. How do you type a tuple value that only contains the integer 42?
#  
#     tp= (42,)
#     

#  15. How do you get a list value's tuple form? How do you get a tuple value's list form?
#    
#    list from tuple
#    
#    l1= (1,2)
#    
#    l2= list(l1)
#    
#    tuple from list
#    
#    l3 = tuple(l2)

# 16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain?
#    
#     variable contains only list value and list itself contains the value.
#    
# 

# 17. How do you distinguish between copy.copy() and copy.deepcopy()?
#  
#     copy.copy creates the copy of the refrence object and copy.deepcopy creates new object of the object.
# 

# In[ ]:




