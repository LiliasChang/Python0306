
# coding: utf-8

# In[1]:


X=1


# In[2]:


X


# In[5]:


type(X)


# In[6]:


type(99.9)


# In[7]:


type('abc')


# In[10]:


print(keyword.kwlist)


# In[11]:


5


# In[12]:


05


# In[13]:


5+5*5/5-5


# In[14]:


2**3


# In[15]:


divmod(9,5)


# In[16]:


2+3*4


# In[17]:


int(98.6)


# In[18]:


int('99')


# In[19]:


int('-23')


# In[20]:


int('+23')


# In[21]:


int('')


# In[22]:


int('1.0e4')


# In[23]:


int('99.9')


# In[24]:


int(1.0e4)


# In[25]:


int(true)


# In[26]:


int(True)


# In[27]:


int(True+2)


# In[28]:


float(True)


# In[29]:


float(False)


# In[30]:


float(99)


# In[31]:


float('99')


# In[32]:


float('0.e4')


# In[33]:


sss='"sers'


# In[34]:


print(sss)


# In[35]:


es='a\nb\nc'


# In[36]:


print(es)


# In[37]:


ee='"\iser\'


# In[38]:


print("'\'ser\")


# In[39]:


print('"\"ser\')


# In[40]:


print('"\"123')


# In[41]:


'123'+'456'


# In[42]:


'123' '456'


# In[43]:


a='鴨'
b=a
c="鴨叫"
a+b+c


# In[45]:


a='鴨'*3+'\n'
b='牛'*4+'\n'
c='吃草'
print(a+b+c)


# In[46]:


joke = '''一二三四五
六七八九六'''


# In[47]:


joke = '123
67890'


# In[48]:


joke = '''一二三四五
六七八九六'''
joke[0]


# In[49]:


joke[2]


# In[50]:


joke[-2]


# In[51]:


joke[11]


# In[52]:


name='lilias'
name[0]='L'


# In[53]:


name.replace('l','L')


# In[54]:


name


# In[55]:


name = name.replace('l','L')


# In[56]:


name


# In[57]:


name='lilias'
'L'+name[:1]


# In[58]:


'L'+name[1:]


# In[59]:


name[0:]


# In[62]:


name[0:5:1]


# In[63]:


name[0:5:-1]


# In[65]:


name[5:0:-1]


# In[66]:


name[::1]


# In[67]:


name[::-1]


# In[68]:


len(name)


# In[69]:


str(98.6)


# In[70]:


aaa=''
len(aaa)


# In[71]:


name.split('*')


# In[72]:


bbb="123,456,789"
bbb.split(',')


# In[73]:


ccc='456*789*000'
ccc.split('*')


# In[74]:


bbb.split()


# In[75]:


ddd='&'
ddd.join(ccc)


# In[77]:


bbb.startword('1')


# In[78]:


a='123....'
a.strip('.')

