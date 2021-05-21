#!/usr/bin/env python
# coding: utf-8

# 1. How do you distinguish between shutil.copy() and shutil.copytree()?
# 
#     shutil.copy() method in Python is used to copy the content of source file to destination file or directory. 
#     hutil.copytree() method recursively copies an entire directory tree rooted at source (src) to the destination directory. The     destination directory, named by (dst) must not already exist. It will be created during copying.

#  2. What function is used to rename files?
#    
#      os.rename()

# 3. What is the difference between the delete functions in the send2trash and shutil modules?
#    
#     The send2trash functions will move a file or folder to the recycle bin, while shutil functions will permanently delete files     and folders.

# 4. ZipFile objects have a close() method just like File objects’ close() method. What ZipFile method is
# equivalent to File objects’ open() method?
#   
#     Yes Zipfile method is equivalent to file objects open() method.

#  5.Create a programme that searches a folder tree for files with a certain file extension (such as .pdf
# or .jpg). Copy these files from whatever location they are in to a new folder.

# In[3]:


import os, shutil

def moveFileType(folder):
    for folderName, subfolders, filenames in os.walk(folder):
        for subfolder in subfolders:
            for filename in filenames:
                if filename.endswith('.jpg'):
                    shutil.copy(folder + filename, '<destination>')

moveFileType('<source>')

