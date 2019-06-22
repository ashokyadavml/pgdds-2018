#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sqlalchemy import create_engine


# In[2]:


import pandas as pd


# In[27]:


salesdata=pd.read_csv('C:/Users/ayadav/Desktop/pgdds/hadoop/assignment2/SalesJan2009_1.csv')
# Be careful of the forward slashes in pandas with windows otherwise
# It creates problem recognising the file path


# In[29]:


myeg=create_engine('sqlite:///:memory:')


# In[30]:


salesdata.to_sql('sales_table', myeg)


# In[35]:


qr1=pd.read_sql_query('SELECT t1.country, t1.state, SUM(t1.price) FROM (SELECT * FROM `sales_table` WHERE payment_type = \'Visa\')t1 GROUP BY t1.country, t1.state', myeg)


# In[40]:


qr2=pd.read_sql_query('SELECT country, AVG(price) FROM `sales_table` GROUP BY country ORDER BY country, AVG(Price)', myeg)


# In[51]:


qr1.to_excel('C:/Users/ayadav/Desktop/pgdds/hadoop/assignment2/query1.xlsx')


# In[52]:


qr2.to_excel('C:/Users/ayadav/Desktop/pgdds/hadoop/assignment2/query2.xlsx')


# In[ ]:




