#!/usr/bin/env python
# coding: utf-8

# 1. Is the Python Standard Library included with PyInputPlus?
#   
#      pyIntplus is not the part of standard library.

# 2. Why is PyInputPlus commonly imported with import pyinputplus as pypi?
# 
#    pyinputsplus are not standard library of python so we have to import it externely and for convention it gives name as pypi.

# 3. How do you distinguish between inputInt() and inputFloat()?
# 
#     inputint() only takes  user input as integer where as inputFloat() only takes input from user as float.

# 4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?

# In[ ]:


import pyinputplus as pyip
result = pyip.inputInt(min = 0 , max = 99)
    


# 5. What is transferred to the keyword arguments allowRegexes and blockRegexes?
#  
#    The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the              PyInputPlus function will accept or reject as valid input.

# 6. If a blank input is entered three times, what does inputStr(limit=3) do?
# 
#     After blank input three times it gives an error of RetryLimit Expection.

# 7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do?
# 
#    it doesnt gives any error after three times it sets the input value of string is hello.

# In[ ]:




