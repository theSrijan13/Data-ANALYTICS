#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[3]:


import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv('911.csv')


# In[5]:


df.head()


# In[6]:


df['zip'].value_counts


# In[8]:


df['twp'].value_counts().head(5)


# In[9]:


df['title'].unique()


# In[10]:


x=df['title'].iloc[0]
x.split(':')[0]


# In[11]:


df['Reason']=df['title'].apply(lambda title:title.split(':')[0])


# In[12]:


df['Reason'].value_counts()


# In[15]:


sns.countplot(x='Reason',data=df,palette='viridis')


# ## let us begin to focus on time information

# In[16]:


df['timeStamp'].iloc[0]


# In[17]:


# convert the coloumns from strings to date time object

df['timeStamp']=pd.to_datetime(df['timeStamp'])


# In[18]:


type(df['timeStamp'].iloc[0])


# In[19]:


time=df['timeStamp'].iloc[0]
time.hour


# In[20]:


time.month


# In[21]:


df['Hour']=df['timeStamp'].apply(lambda time:time.hour)


# In[22]:


df['Hour']


# In[23]:


df['Month']=df['timeStamp'].apply(lambda time:time.month)
df['Day of Week']=df['timeStamp'].apply(lambda time:time.dayofweek)


# In[24]:


df.head()


# # lets map strings to actual days of week
# 

# In[25]:


dmap={0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week']=df['Day of Week'].map(dmap)


# In[26]:


df.head()


# # using seaborn to create a countplot of the day of week coloumn with hue based off the reason column

# In[28]:


sns.countplot(x='Day of Week',data=df,hue='Reason')


# In[29]:


byMonth=df.groupby('Month').count()


# In[30]:


byMonth.head()


# In[31]:


byMonth['lat'].plot()


# In[32]:


sns.countplot(x='Month',data=df)
plt.legend(bbox_to_anchor(1.05,1),loc=2,borderaxespad=0)


# In[33]:


sns.lmplot(x='Month',y='twp',data=byMonth.reset_index())


# In[34]:


t=df['timeStamp'].iloc[0]


# In[35]:


t


# In[36]:


t.date()


# In[37]:


df['Date']=df['timeStamp'].apply(lambda t:t.date())
df.head()


# In[39]:


df.groupby('Date').count()['lat'].plot()
plt.tight_layout()


# In[41]:


df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('traffic')
plt.tight_layout()


# In[43]:


df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()


# In[44]:


df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()


# In[48]:


dayHour=df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()


# In[49]:


sns.heatmap(dayHour)


# In[50]:


sns.clustermap(dayHour)


# In[ ]:




