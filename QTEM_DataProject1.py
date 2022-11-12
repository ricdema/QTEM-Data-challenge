#!/usr/bin/env python
# coding: utf-8

# # QTEM DATA PROJECT

# ### First we'll run the Panda Explanatory Data Analysis Module

# In[3]:


#pip install pandas-profiling


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_profiling import ProfileReport


# In[8]:


### Define datasets

df_calls = pd.read_csv("b. CARTIER_CALLS.csv")
df_clienteling = pd.read_csv("c. CARTIER_CLIENTELING.csv")
df_livechat = pd.read_csv("d. CARTIER_LIVECHAT.csv")
df_prevsales = pd.read_csv("e. CARTIER_PREVIOUS_SALES.csv")
df_sales = pd.read_csv("f. CARTIER_SALES.csv")
df_wishlist = pd.read_csv("g. CARTIER_WISHLIST.csv")


# In[10]

# Create new column so we can identify which record comes from Sales and which comes from previous sales once we merge both datasets

df_sales['salesdataset']=1
df_prevsales['salesdataset']=0

print(df_sales.head(1), df_prevsales.head(1))

# In[9]


###Sort the datasets by Invoice Number 

#df_sales.sort_values(by='ClientID', ascending=False)
#df_prevsales.sort_values(by='ClientID', ascending=False)


# In[10]:


### Create sample dataset out of the merged sales and prev sales datasets that is 10% of total size of parent

df_allsales = pd.concat([df_sales, df_prevsales])
df_allsales = df_allsales.sort_values(by='ClientID', ascending= True)

df_allsalessample10 = df_allsales.head(int(round((len(df_allsales)/(10)),0)))


# In[11]


# In[48]:


print(list(df_allsalessample10))


# In[49]:


# Sort according to client ID

df_allsalessample10 = df_allsalessample10.sort_values(by='ClientID', ascending=True)


# In[18]:


# Let's createa a column that will count how many times a Client appears in the DB

#df_allsalessample10['Counts_ClientID'] = df_allsalessample10.groupby(['ClientID'])['InvoiceHeader'].transform('count')


# In[38]:


# Sort according to number of appearance of a client ID

##df_allsalessample10.sort_values(by='Counts_ClientID', ascending=False)


# In[27]:


### Profile for previous sales
#profile_prevsales = ProfileReport(df_prevsales, title="Pandas Profiling Report Previous Sales")

### Profile for Sales
#profile_sales = ProfileReport(df_sales, title="Pandas Profiling Report Sales")


# In[14]:


## Visualizing the reports

#profile.to_notebook_iframe()
#profilesales.to_notebook_iframe()


# In[28]:


## Report to HTML
#profile.to_file(output_file='output.html')
#profile_sales.to_file("profile sales")
#profile_prevsales.to_file("profile previous sales")




# In[38]:


# df_sales = df_sales.astype({"TransactionDate": datetime64,
#                   "TransactionDate_FYYYY": datetime64,
#                   "AgeAtTransaction": int64, 
#                   "PersonBirthDate": datetime64, 
#                   "WeddingDate": datetime64,
#                   "FirstSalesDate": datetime64,
#                  "FirstTransactionDate": date64,
#                  })


# In[44]:


### Export sample df to csv

#dfsales_sample10.to_csv('CartierSalesSample.csv') 
#dfprevsales_sample10.to_csv('CarterPreviousSalesSample.csv')
df_allsalessample10.to_csv('allsalessample10sorted.csv') 



# In[46]:


### Profile for previous sales Sample
#profile_prevsalessample = ProfileReport(df_prevsales, title="Pandas Profiling Report Previous Sales Sample")

### Profile for Sales Sample
#profile_salessample = ProfileReport(df_sales, title="Pandas Profiling Report Sales Sample")

### Export to HTML

#profile_salessample.to_file("profile sales Sample.html")
#profile_prevsalessample.to_file("profile previous sales Sample.html")


# In[ ]:

print(df_allsalessample10['ClientID'].head(20))


