#!/usr/bin/env python
# coding: utf-8

# 1. What are escape characters, and how do you use them?
#  
#     \' - for single quote 
#      print("this is mohan\'s house")
#      
#     \" - double quote 
#     print("this is \"mohan\", house")
#     
#     \n - New line 
#       print("this is mohan\n my  house")
#         
#     \t - New tab    
#       print("this is mohan\t my  house")

# 2. What do the escape characters n and t stand for?
#     
#     The space characters n and t stands for new line and new tab.

# 3. What is the way to include backslash characters in a string?
# 
#    str = "ok I\'m ready"

# 4. The string "Howl's Moving Castle" is a correct value. Why isn't the single quote character in the word Howl's not escaped a problem?
#    
#    Because the whole string are encapsulated by quotes.

# 5. How do you write a string of newlines if you don't want to use the n character?
#   
#     New line in os package. it is called linesep.

# 6. What are the values of the given expressions?
# 
# 'Hello, world!'[1]
#   e
#     
# 'Hello, world!'[0:5]
#  'Hello'
# 
#  'Hello, world!'[:5]
#   'Hello'
# 
#  'Hello, world!'[3:]
#   'lo, world!'
# 

#  7. What are the values of the following expressions?
# 

# In[13]:


'Hello'.upper()


# In[14]:


'Hello'.upper().isupper()


# In[15]:


'Hello'.upper().lower()


# 8. What are the values of the following expressions?
# 
# 

# In[16]:


'Remember, remember, the fifth of July.'.split()


# In[17]:


'-'.join('There can only one.'.split())


# 9. What are the methods for right-justifying, left-justifying, and centering a string?
#    
#    ljust(10, *), rjust(10, *), center(10, *)

# 10. What is the best way to remove whitespace characters from the start or end?
#  
#       The best way to rempove space from the start and end rstrip(), and lstrip().

# 

# In[ ]:




