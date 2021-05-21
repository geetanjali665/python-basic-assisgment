#!/usr/bin/env python
# coding: utf-8

# 1.   What are the two values of the Boolean data type? How do you write them?
#      
#      There are two types of boolen data. True or False.

# 2. What are the three different type of boolean operator?
#    
#    The logical operator and , or and not are reffered as boolean operator.

# 3. Make a list of each Boolean operator's truth tables (i.e. every possible combination of Boolean values for the operator and    what it evaluate )
#    
#     And operator :-  
#     
#     
#     True - True = True
#     True - False = False
#     False - True = False
#     False - False = False
#     
#     
#     OR operator:-
#         
#         True - True = True
#         True - False = True
#         False - False = False
#         False - True = True
#         
#     And operator:-
#         
#         True - False
#         False - True
#         

# 4. What are the values of the following expressions?
# 
#    (5 > 4) and (3 == 5) = False
#     
#    not (5 > 4) = False
# 
#    (5 > 4) or (3 == 5) = True
#     
#    not ((5 > 4) or (3 == 5)) = False
# 
#    (True and True) and (True == False) = False
#     
#    (not False) or (not True) = True
# 

# 5. What are the six comparison operators?
#    
#    
#     1. greater than(>)
#     2. Less than (<)
#     3. greater than or equal (>=)
#     4. less than or equal (<=)
#     5. equals to equals(==)
#     6. Not equals to(!=)

# 6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
#   
#     The difference between equals to or assigment operator is when we assign any value to a variable then we use assigment operator
#     but when we make any comparsion then we use equal operator.
#     
#     condition:
#          if we have to assign 12 into a variable then we use assigment operator as a = 12
#          
#          if we have to make any comparison then we use equal operator as 
#             if a == 12:
#                 print("hello")

#   7. Identify the three blocks in this code:
# 
# 
#      spam = 0
#    
#      if spam == 10:
#         
#      print('eggs')
#    
#      if spam > 5:
#         
#      print('bacon')
#    
#      else:
#         
#      print('ham')
#      print('spam')
#      print('spam')
# 
#      There are three blocks in this code two if block and one else block.
# 

# 8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
#    

# In[6]:


spam = 1
if spam == 1:
    print("1")
elif spam == 2:
    print("Howdy")
else:
    print("Greeting!")
    
    


# 9. If your programme is stuck in an endless loop, what keys you’ll press?
#    
#     ctrl+c or ctrl+c+enter
#    

# 10. How can you tell the difference between break and continue?
#     
#     The main difference between break and continue statement is that when break keyword is encountered, it will exit the loop.
#     and continue statement gives immediate command to the loop and forces to excutes the next iteration

# 11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
#     
#     There is no difference in these three statement in for loop.

# 12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

# In[17]:


for i in range(1,11):
    print(i)


# In[19]:


i = 0
while(i<=10):
    print(i)
    i+=1


# 13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
#     
#     spam.bacon()
