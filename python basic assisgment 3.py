#!/usr/bin/env python
# coding: utf-8

# 1. Why are functions advantageous to have in your programs?
#    
#     when we have functions in our programs we can called it multiple times so it increses the code reusebility of program and also decreases the size of the program not by writing the same things again and again.

# 2. When does the code in a function run: when it's specified or when it's called?
# 
#    when it's specified

# 3. What statement creates a function?
#    
#     def geet():

# 4. What is the difference between a function and a function call?
#   
#     The difference between the function and function call is, A function is procedure to achieve a particular result while         function call is using this function to achive that task.

# 5. How many global scopes are there in a Python program? How many local scopes?
#    
#    There are one global and and the number of local scopes creates inside the function is referred as local scope.

# 6. What happens to variables in a local scope when the function call returns?
# 
#    When the function returns, the local scope is destroyed, and these variables are forgotten.

# 7. What is the concept of a return value? Is it possible to have a return value in an expression?
#    
#    The concept of return value is when we call any function what its gives and output is defined as return value of a function.
#    yes it is possible having return value in expression.

# 8. If a function does not have a return statement, what is the return value of a call to that function?
#    
#    None

# 9. How do you make a function variable refer to the global variable?
#   
#      

# In[5]:


x = 10
def function_call():
    global x
    print(x)
        
        
function_call()


# 10. What is the data type of None?

# In[2]:


type(None)


# 12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
#     
#    bacon() called function inside spammodule
#       spam.bacon()

# 13. What can you do to save a programme from crashing if it encounters an error?
#    
#      write the code that may cause an error in try block and except the error to save the programme from crashing if it encounters an error.

# 14. What is the purpose of the try clause? What is the purpose of the except clause?
# 
#    The purpose of try block to save the programme from crashing if it encounters any error so that all other function runs        without any problem. and the purpose of except block to catch the error.
#     
