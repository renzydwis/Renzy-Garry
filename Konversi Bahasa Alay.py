#!/usr/bin/env python
# coding: utf-8

# In[26]:


#PR Konversi Kata Alay
kata_awal = input('masukkan kata : ')  
kata_baru = ""
for i in kata_awal:
    if i == 'a':
        kata_baru += ' @ '
    elif i == 'g':
        kata_baru += ' 9 '
    elif i == 'o':
        kata_baru += ' 0 '
    elif i == 'e':
        kata_baru += ' 3 '
    else:
        kata_baru += i
kata_baru += '...'
print(kata_baru)


# In[ ]:





# In[16]:




