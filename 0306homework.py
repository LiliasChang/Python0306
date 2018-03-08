
# coding: utf-8

# In[5]:


import requests
response = requests.get('''http://www.novelscape.net/wxxs/j/jingyong/ffwz/001.htm''')
response.encoding = "big5"
book1 = response.text
book1


# In[23]:


book1[1300:1350]


# In[26]:


print(book1[1300:1350])


# In[25]:


book1.find('<TITLE>')


# In[27]:


print(book1[book1.find('<TITLE>') + len('<TITLE>'):book1.find('</TITLE>')])


# In[28]:


book1.startswith('<html>')


# In[29]:


book1.lower().startswith('<html>')


# In[30]:


book1.lower().endswith('</html>')


# In[40]:


print(book1[book1.find('<TITLE>') + len('<TITLE>'):book1.find('</TITLE>')].replace("第一章","第二章"))


# In[41]:


book1.lower().find('html')


# In[42]:


book1.lower().rfind('html')


# In[44]:


len(book1)


# In[45]:


book1.find("第一章")


# In[46]:


book1[book1.find("第一章"):book1.find("</TITLE>")]


# In[59]:


a = book1[1300:1400]

b = book1[2000:2500:5]


# In[64]:


a


# In[65]:


b


# In[69]:


'<BR>'.join(a)

