#!/usr/bin/env python
# coding: utf-8

# 1. What does an empty dictionary's code look like?
#   
#   d1= {}
# 
# 

# 
# 2. What is the value of a dictionary value with the key 'foo' and the value 42?
# 
#    d1 = {"foo" : 42}

# 3. What is the most significant distinction between a dictionary and a list?
#    
#      List and dictionary are both different data structure in list we generally store the value in a certain order so we can index in the list where in dictionary we have assosiate values with keys.

# 
# 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
#    
#     it gives key error

# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
# 
#     Both are same expression.

# 
# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
# 
#    Cat in spam check that there is any key in spam like cat and gives true and false and 'cat' in spam.values() gives valu        associate with cat key.
# 

# In[ ]:



get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')

if 'color' not in spam:
spam['color'] = 'black'

  

  



# 8. How do you "pretty print" dictionary values using which module and function?
#   
#     The module are pprint and function pprint
# 
