#!/usr/bin/env python
# coding: utf-8

# # Week 1: Getting started with Anaconda, Jupyter Notebook and Python

# a) Why you chose to join this course – for, motivation, vision, aspiration?
# 
# I chose to join this course because for the past two years I have enjoyed many aspects of what I have learned so far. Each topic is encouraging me to use my creativity and skill to excel in this course, hopefully to find a job in the future that focuses on this field of expertise.

# b) Prior experience, if any, you have with AI and/or Python, and, 
# 
# I have prior knowledge of html but no experience with Python. So I am willing to learn as much as possible.

# c) What you expect to learn from the course (aim for 3-5 bullet points)
# 
# - To have a better understanding of AI, how it can be useful or dangerous.
# - To be able to use Python effectively.
# - To have a conclusive opinion about Ai with my new knowledge. 

# In[11]:


intro = (" Hello, World ")
print (intro)


# In[5]:


from IPython.display import*


# In[6]:


YouTubeVideo ("Q2JLmAx6drs")


# In[ ]:


import webbrowser
import requests
print("Shall we hunt down an old website?")
site = input("Type a website URL: ")
era = input("Type year, month, and date, e.g., 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = requests.get(url)
data = response.json()
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("Found this copy: ", old_site)
    print("It should appear in your browser.")
    webbrowser.open(old_site)
except:
    print("Sorry, could not find the site.")


# # Week 2: Exploring Data in Multiple Ways

# In[2]:


from IPython.display import*


# In[4]:


Image ("picture1.jpg")


# In[6]:


from IPython.display import*


# In[8]:


Audio ("audio1.mid")


# In[10]:


from IPython.display import*


# In[12]:


Audio ("audio2.ogg")


# In[15]:


# The sound file audio2.ogg is owned by Artoffuge Mehmet Okonsar.
# This file is licensed under the Creative Commons Attribution-Share Alike 3.0 Unported license.
# The original ogg file was found at the url: 
url= https://en.wikipedia.org/wiki/File:GoldbergVariations_MehmetOkonsar-1of3_Var1to10.ogg


# In[21]:


from matplotlib import pyplot
test_picture = pyplot.imread("picture1.jpg")
print("Numpy array of the image is: ", test_picture)
pyplot.imshow(test_picture)


# # Week Three: Exploring Scikit-learn

# In[31]:


from sklearn import datasets


# In[32]:


dir(datasets)


# I chose this as it seemed interesting to explore.

# In[34]:


iris_data = datasets.load_iris()


# In[35]:


iris_data.DESCR


# In[36]:


print (iris_data.DESCR)


# In[37]:


iris_data.feature_names


# In[38]:


iris_data.target_names


# In[41]:


from sklearn import datasets
import pandas

iris_data = datasets.load_iris()

iris_dataframe = pandas.DataFrame(data=iris_data['data'], columns = iris_data['feature_names'])


# In[ ]:




