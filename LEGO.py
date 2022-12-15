#!/usr/bin/env python
# coding: utf-8

# In[3]:


#import our libraries
import pandas as pd
import numpy as np


# In[6]:


#import our first dataset sets.csv 
df_sets = pd.read_csv(r'C:\Users\conno\Downloads\sets.csv')


# In[7]:


#import our second dataset themes.csv
df_themes = pd.read_csv(r'C:\Users\conno\Downloads\themes.csv')


# In[8]:


#print the first five rows of the first data set
df_sets.head()


# In[9]:


#print the first five rows of the second data set
df_themes.head()


# In[12]:


#expore the data
#check datatypes
df_sets.dtypes


# In[11]:


#check datatypes
df_themes.dtypes


# In[13]:


#check data distribution
df_sets.describe()


# In[14]:


#check data distribution
df_themes.describe()


# In[15]:


#check for nulls
df_sets.isnull().sum()


# In[16]:


#check for nulls
df_themes.isnull().sum()


# In[ ]:


#we could remove the rows with nulls, but we aren't going to use the column parent_id in this analysis
#df_themes.dropna(inplace=True)


# In[18]:


#check for duplicate rows
df_sets.duplicated()


# In[19]:


#check for duplicate rows
df_themes.duplicated()


# In[20]:


#check for outliers
df_sets.boxplot(column='year')


# In[ ]:




