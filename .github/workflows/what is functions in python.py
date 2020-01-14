#!/usr/bin/env python
# coding: utf-8

# In[28]:


x=6
def abc(x):
    return 9*x


# In[29]:


a=abc(5)
print(a)


# In[31]:


b=abc(10)
print(b)


# In[32]:


def xy(x,y):
    return x+y


# In[33]:


c=xy(5,89)
print(c)


# In[38]:


def zz(x):
    print(x)
    print("still in the functions")
    return x*88
e= zz(67)
print(e)


# In[42]:


def abdullah(name,fname,reg_no,institute,course):
    text="""
"STUDENT ID CARD"             
    Name =  {}                    
    Father Name=  {}              
    Registration number=  {}      
    University name=  {}
    Course=  {}""".format(name,fname,reg_no,institute,course)
    print(text)
    
abdullah("Muhammad Abdullah","Muhammad Arif","FA18-BSE-028","COMSTATS UNIVERSITY ISLAMABAD(wah)","Software Engineering")


# In[ ]:




