#!/usr/bin/env python
# coding: utf-8

# In[65]:


import pandas as pd
import matplotlib.pyplot as plt


# In[10]:


#Import Dataset 
data = pd.read_csv("surveyfile.csv")
data.head()


# In[32]:


data.info()


# In[67]:


#getting data with positive mental health consequences
mental_health_consequence_yes=data[data['mental_health_consequence'].str.contains("Yes")]
mental_health_consequence_yes.head()


# In[68]:


#adding further columns affecting the mental health
mental_health_location=mental_health_consequence_yes[mental_health_consequence_yes['leave'].str.contains("Very easy")]
mental_health_location.head()


# In[50]:


#getting the count
mental_health_location_hist = mental_health_location.groupby(['Country'])['mental_health_consequence'].count()


# In[51]:


#printing the output
print(mental_health_location_hist)


# In[53]:


#filtering to a specific country
mental_health_location_uniquecountry = mental_health_location[mental_health_location['Country'].str.contains("Canada")].groupby(['Country'])['mental_health_consequence'].count()


# In[54]:


#getting the output
print(mental_health_location_uniquecountry)


# In[66]:


#line plot
mental_health_location_hist.plot.line()
plt.ylabel('Count')


# In[ ]:





# In[ ]:




