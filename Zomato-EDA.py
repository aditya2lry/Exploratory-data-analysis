#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('zomato.csv',encoding='latin-1')
df.head()


# In[3]:


df.columns


# In[4]:


df.info()


# In[5]:


df.describe()


# # In Data Analysis what all things we do
# 1.missing values
# 2.Explore Above the Numerical Variables
# 3.Explore about categorical Variables
# 4.Finding Relationship between features

# In[6]:


df.isnull().sum()


# In[7]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[8]:


df_country=pd.read_excel('Country-Code.xlsx')
df_country.head()


# In[9]:


df.columns


# In[10]:


df_final=pd.merge(df,df_country,on='Country Code',how='left')


# In[11]:


df_final.head()


# In[12]:


df_final.dtypes


# In[13]:


df_final.columns


# In[14]:


country_names=df_final.Country.value_counts().index


# In[15]:


country_names


# In[16]:


country_val=df_final.Country.value_counts().values


# In[17]:


country_val


# In[18]:


## pie chart top 5 country 
plt.pie(country_val[:3],labels=country_names[:3],autopct='%1.2f%%')


# Observation:Zomato maximumum records or transaction is from india after that USA and then UK

# In[19]:


ratings=df_final.groupby(['Aggregate rating','Rating color','Rating text']).size().reset_index().rename(columns={0:'rating Count'})


# In[20]:


ratings


# # conclusion:
# 1.whenever the rating is between 4.5 to 4.9 ---> Excellent 
# 2.whenever the rating is between 4.0 to 3.4 ---> very good
# 3.whenever the rating is between 3.5 to 3.9 ---> good
# 4.whenever the rating is between 3.0 to 3.4 ---> Average
# 5.whenever the rating is between 2.5 to 2.9 ---> Average
# 6.whenever the rating is between 2.0 to 2.4 ---> poor

# In[21]:


sns.barplot(x='Aggregate rating',y='rating Count',data=ratings)


# In[22]:


sns.barplot(x='Aggregate rating',y='rating Count',hue='Rating color',data=ratings)


# In[23]:


##Arranging the color with respect to their name
sns.barplot(x='Aggregate rating',y='rating Count',hue='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# # observation
# 1.Not Ratted is very high 
# 2.maximum number of ratting is between 2.5 to 3.4

# In[24]:


## count plot
sns.countplot(x='Rating color',data=ratings,palette=['blue','red','orange','yellow','green','green'])


# In[25]:


### find the countries names that has been given zero rating 
df_final[df_final['Rating color']=='White'].groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# #Obsevation: Maximum number of 0 ratings froms indian customers

# In[26]:


##find out which currency is used by which country
df_final.columns


# In[27]:


df_final[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[28]:


##find out which countries do Have Online delivery
df_final[df_final['Has Online delivery']=='YES'].Country.value_counts()


# In[29]:


df_final[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# ##Observation :
#     1.Online deliveries are available in india and UAE

# In[30]:


##create a pie chart for city distribution


# In[31]:


city_label=df_final.City.value_counts().index


# In[32]:


city_val=df_final.City.value_counts().values


# In[33]:


plt.pie(city_val[:5],labels=city_label[:5],autopct='%1.2f%%')


# In[34]:


## find the top 10 cuisines
cuisines_label=df_final.Cuisines.value_counts().index
cuisines_val=df_final.Cuisines.value_counts().values


# In[35]:


plt.pie(cuisines_val[:10],labels=cuisines_label[:10],autopct='%1.2f%%')


# In[45]:


df_final.Cuisines.value_counts()
#.sort_values(ascending=False).head(10)


# In[ ]:





# In[ ]:




