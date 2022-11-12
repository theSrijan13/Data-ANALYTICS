#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install DataReader


# In[2]:


pip install pandas-datareader


# In[3]:


from pandas_datareader import data, wb
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


start=datetime.datetime(2006,1,1)
end=datetime.datetime(2016,1,1)


# In[5]:


BAC=data.DataReader('BAC','yahoo',start,end)
#CITI BANK
C = data.DataReader("C", "yahoo", start, end)
# GOLDMAN SACHS
GS = data.DataReader("GS", "yahoo", start, end)
# JP MORGAN CHASE
JPM = data.DataReader("JPM", "yahoo", start, end)
# MORGAN STANLEY
MS = data.DataReader("MS", "yahoo", start, end)
#WELLS FARGO
WFC = data.DataReader("WFC", "yahoo", start, end)


# In[6]:


BAC


# # CREATE A LIST OF TICKER SYMBOLS IN ALPHABETICAL ORDER

# In[7]:


tickers=['BAC','C','GS','JPM','MS','WFC']


# ## USE pd.concat to concatanate dataframes together into a single dataframe called bank_stocks. Set keys arguments equal to tickers list

# In[8]:


bank_stocks=pd.concat([BAC,C,GS,JPM,MS,WFC],axis=1,keys=tickers)
bank_stocks.head()


# ## set the coloumn name levels 

# In[9]:


bank_stocks.columns.names=['Bank Ticker','Stock Info']


# In[10]:


bank_stocks.head()


# ## estimating the max close price for each bank's stocks

# In[11]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').max()


# ## Create a new empty dataframe called returns. It will contain the return of each bank account

# In[12]:


returns=pd.DataFrame()


# ## we can use pct_change() method on the close column to create a column representing return value

# In[13]:


for tick in tickers:
    returns[tick+'Return']=bank_stocks[tick]['Close'].pct_change()


# In[14]:


returns.head()


# In[15]:


sns.pairplot(returns[1:])


# ## finding out on which day bank had  the best and worst single day return

# In[16]:


returns.idxmin()


# In[17]:


returns.idxmax()


# ## take a look at the standard deviation of the return 

# In[18]:


returns.std()


# In[19]:


returns.head()


# In[24]:


returns.ix['2015-01-01':'2015-12-31'].std()


# ## create a displot for 2015 returns of morgan stanley

# In[23]:


sns.displot(return.ix['2015-01-01':'2015-12-31']['MS Return'],color='green')


# In[25]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
get_ipython().run_line_magic('matplotlib', 'inline')
import plotly
import cufflinks as cf
cf.go_offline()


# ## create a line plot showing close price for each bank

# In[26]:


for tick in tickers:
    bank_stocks[tick]['Close'].plot(label=tick,figsize=(12,4))
plt.legend()


# In[28]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info')


# In[29]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').plot()


# In[30]:


bank_stocks.xs(key='Close',axis=1,level='Stock Info').iplot()


# In[32]:


sns.heatmap(bank_stocks.xs(key='Close',axis=1,level='Stock Info').corr(),annot=True)


# In[ ]:




