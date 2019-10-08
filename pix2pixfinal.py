#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('git clone https://github.com/affinelayer/pix2pix-tensorflow.git')


# In[ ]:


from google.colab import files
files.upload()


# In[ ]:


get_ipython().system('pip install -q kaggle')


# In[ ]:


get_ipython().system('mkdir -p ~/.kaggle')
get_ipython().system('cp kaggle.json ~/.kaggle/')


# In[ ]:


get_ipython().system('kaggle datasets download -d saisriteja/project1')


# In[ ]:


get_ipython().system('unzip project1.zip')


# In[ ]:


cd pix2pix-tensorflow


# In[ ]:


get_ipython().system('python tools/download-dataset.py facades')


# In[ ]:


get_ipython().system('mkdir output')


# In[ ]:


get_ipython().system('python pix2pix.py   --mode train   --output_dir output   --max_epochs 200   --input_dir /content/new/train   --which_direction BtoA')


# In[ ]:


get_ipython().system('mkdir res')


# In[ ]:


get_ipython().system('python pix2pix.py   --mode test   --output_dir res   --input_dir /content/new/test   --checkpoint output')


# In[ ]:


get_ipython().system('zip -r res.zip res')


# In[ ]:


get_ipython().system('zip -r output.zip output')


# In[ ]:




