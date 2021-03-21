#!/usr/bin/env python
# coding: utf-8

# In[111]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import lag_plot


# In[112]:


df = pd.read_csv("./14100355.csv", usecols = ['REF_DATE', 'GEO', 'North American Industry Classification System (NAICS)','Statistics','Data type','VALUE'])
ds =  pd.read_csv("./14100355.csv", usecols = ['REF_DATE', 'GEO', 'North American Industry Classification System (NAICS)','Statistics','Data type','VALUE'])


# In[113]:


df = df.rename(columns = {"North American Industry Classification System (NAICS)":"Industry"})
ds = ds.rename(columns = {"North American Industry Classification System (NAICS)":"Industry"})


# In[114]:


df = df[(df['GEO'] =='Ontario') & (df['Industry'] == 'Educational services [61]') & (df['REF_DATE'].between(("2015-01"),("2021-01"))) & (df['Statistics'] == 'Estimate') & (df['Data type'] == 'Unadjusted')]
ds = ds[(ds['GEO'] =='Ontario') & (ds['Industry'] == 'Health care and social assistance [62]') & (ds['REF_DATE'].between(("2015-01"),("2021-01"))) & (ds['Statistics'] == 'Estimate') & (ds['Data type'] == 'Unadjusted')]
print(ds[(ds['GEO'] =='Ontario') & (ds['Industry'] == 'Health care and social assistance [62]') & (ds['REF_DATE'].between(("2015-01"),("2021-01"))) & (ds['Statistics'] == 'Estimate') & (ds['Data type'] == 'Unadjusted')]
)


# In[93]:


df.month = pd.to_datetime(df.REF_DATE)
df.set_index('REF_DATE', inplace=True)

ds.month = pd.to_datetime(ds.REF_DATE)
ds.set_index('REF_DATE', inplace=True)


# In[94]:


df.plot(figsize=(30,8), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[95]:


val1 = df[['VALUE']]
val1.rolling(12).mean().plot(figsize=(30,8), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[96]:


ds.plot(figsize=(30,8), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[97]:


val2 = ds[['VALUE']]
val2.rolling(12).mean().plot(figsize=(30,8), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[98]:


df_rm = pd.concat([val1.rolling(12).mean(), val2.rolling(12).mean()], axis=1)
df_rm.plot(figsize=(30,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[99]:


val1.diff().plot(figsize=(30,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[100]:


val2.diff().plot(figsize=(30,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[101]:


sns.lmplot(x='REF_DATE', y='VALUE', fit_reg=False, data=ds')


# In[102]:


df_rm.corr()


# In[103]:


df_rm.plot(figsize=(30,10), linewidth=5, fontsize=20)
plt.xlabel('Year', fontsize=20);


# In[104]:


df_rm.diff().corr()


# In[105]:


pd.plotting.autocorrelation_plot(val1);


# In[106]:


pd.plotting.autocorrelation_plot(val2);


# In[110]:


print(ds[(ds['GEO'] =='Ontario') & (ds['Industry'] == 'Health care and social assistance [62]') & (ds['REF_DATE'].between(("2015-01"),("2021-01"))) & (ds['Statistics'] == 'Estimate') & (ds['Data type'] == 'Unadjusted')]
)


# In[ ]:




