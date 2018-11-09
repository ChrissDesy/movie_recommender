#!/usr/bin/env python
# coding: utf-8

# # Movie Recommendation Based on Content Based Filtering

# #### Stages
# 1. data analysis.
# 2. recommend movies

# In[ ]:





# # Imports

# In[43]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# # Loading the data

# In[44]:


#Reading users file:
u_cols = ['user_id','age','sex','occupation','zip_code']
users = pd.read_csv('data/u.user', sep='|', names=u_cols, usecols=range(5), encoding='latin-1')
#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating','timestamp']
ratings = pd.read_csv('data/u.data', sep='\t', names=r_cols, usecols=range(4), encoding='latin-1')
#Reading movies file:
m_cols = ['movie_id', 'title','release_date','v_release']
movies = pd.read_csv('data/u.item', sep='|', names=m_cols, usecols=range(4), encoding='latin-1')

movrate = pd.merge(movies,ratings)
data = pd.merge(movrate,users)


# In[45]:


data.head()


# # 1. Analyse the data

# ##### show the data to be used

# In[46]:


data


# #### 20 Most rated movies
# movies that have been watched and rated by users

# In[26]:


most_watched = data.title.value_counts()[:20]
most_watched


# In[27]:


most_watched.plot.bar()
plt.title("20 Most watched Movies")
plt.ylabel('Number of ratings')


# figure above is showing the 20 most watched and rated movies by most users. Star wars had the highest number of ratings whilst the least one is Star Trek: First Contact.

# #### Age which frequently watches movies
# Here we are analysing the age group which watches movies the most.

# In[28]:


#frequency in age range
#data['age']
data.age.value_counts()


# In[29]:


users.age.plot.hist()
plt.title("Age Frequency")


# figure above is showing that the age group in the late twenties and early thirties have the highest frequency of watching movies.

# ### Movie ratings
# how the movies are rated

# In[22]:


movie_stats = data.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head()
#movie_stats[:30]


# In[58]:


# sort by rating average
movie_stats.sort_values([('rating', 'mean')], ascending=False)[:30]
atleast_100 = movie_stats['rating']['size'] >= 100
movie_stats[atleast_100].sort_values([('rating', 'mean')], ascending=False)[:30]


# ### Movies ratings by gender
# how movies are rated by gender

# In[76]:


gender_rate = data.pivot_table(index=['movie_id', 'title'],
                           columns=['sex'],
                           values='rating',
                           fill_value=0)
gender_rate[:30]


# In[ ]:





# # 2. Recommendation
# recommendation by Age and Gender using Movie ratings as target variable.

# ### by Age
# recommend system using age

# In[7]:


def reco_age():
    uage = int(input("\nEnter User Age... \t"))
    
    userage = data[data['age']== uage]
    top = userage[userage['rating'] == 5]

    topr = top.drop('movie_id',1)
    topec = topr.drop('user_id',1)
    toprecom = topec.drop('rating',1)

    #create list of movies...
    lst = []
    for item in toprecom['title'][:7]:
        lst.append(item)

    #print the movies
    print("\n\n\tMOVIES YOU MAY LIKE..\n")
    for movi in lst:
          print(movi)


# In[32]:


reco_age()


# ## By Gender
# recommend by gender

# In[35]:


def reco_gen():
    uge = input("\nEnter User Gender (M\F)... \t")
    #print(uge)
    
    gend = data[data['sex'] == uge]
    top = gend[gend['rating'] == 5]

    topr = top.drop('movie_id',1)
    topec = topr.drop('user_id',1)
    toprecom = topec.drop('rating',1)

    #create list of movies...
    lst = []
    for item in toprecom['title'][:7]:
        lst.append(item)

    #print the movies
    print("\n\n\tMOVIES YOU MAY LIKE..\n")
    for movi in lst:
          print(movi)


# In[36]:


reco_gen()


# ## Recom

# In[39]:


def hybrid():
    gen = input("Whats your gender..\t")
    ag = int(input("Whats your age..\t"))
    
    gend = data[data['sex'] == gen]
    top = gend[gend['rating'] == 5]
    toper = top[top['age']== ag]
    
    topr = toper.drop('movie_id',1)
    topec = topr.drop('user_id',1)
    toprecom = topec.drop('rating',1)
    
    #create list of movies...
    lst = []
    for item in toprecom['title'][:7]:
        lst.append(item)
        
    #print the movies
    print("\n\n\tMOVIES YOU MAY LIKE..\n")
    for movi in lst:
          print(movi)
    


# In[40]:


hybrid()


# In[41]:


hybrid()


# # Conclusion

# In[ ]:




