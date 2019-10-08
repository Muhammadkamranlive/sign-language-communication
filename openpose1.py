#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('mkdir data')


# In[ ]:


import os
os.listdir()
os.chdir("/content/data")


# In[ ]:


get_ipython().system('wget ftp://wasserstoff.informatik.rwth-aachen.de/pub/rwth-phoenix/2016/phoenix-2014.v3.tar.gz')


# 

# In[ ]:


os.getcwd()


# In[ ]:


os.listdir()


# In[ ]:


import tarfile
fname='phoenix-2014.v3.tar.gz'
tar = tarfile.open(fname, "r:gz")
tar.extractall()


# In[ ]:


get_ipython().system('wget ftp://wasserstoff.informatik.rwth-aachen.de/pub/rwth-boston-104/rwth-boston-104.tar.gz')


# In[ ]:


path='/content/data/rwth-boston-104.tar.gz'
tar = tarfile.open(path, "r:gz")
tar.extractall()


# In[ ]:


os.chdir('/content')


# In[ ]:


get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --video ../videos.mp4  --display 0 --face --hand --write_video ../output.avi --disable_blending --alpha_pose 1')


# In[ ]:


get_ipython().system('ffmpeg -y -loglevel info -i output.avi  languages.mp4')


# In[ ]:


def show_local_mp4_video(file_name, width=640, height=480):
  import io
  import base64
  from IPython.display import HTML
  video_encoded = base64.b64encode(io.open(file_name, 'rb').read())
  return HTML(data='''<video width="{0}" height="{1}" alt="test" controls>
                        <source src="data:video/mp4;base64,{2}" type="video/mp4" />
                      </video>'''.format(width, height, video_encoded.decode('ascii')))

show_local_mp4_video('languages.mp4', width=960, height=720)


# In[ ]:


get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/001 --display 0 --face --hand --write_images /content/output_heatmaps_folder  --disable_blending --alpha_pose 1  ')


# In[ ]:


get_ipython().system('mkdir skeletonimages/002')


# In[ ]:


get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/002 --display 0 --face --hand --write_images /content/skeletonimages  --disable_blending --alpha_pose 1  ')


# In[ ]:


files=os.listdir('/content/data/png-segments')
len(files)


# In[ ]:


get_ipython().system('mkdir skeletonimage')


# In[ ]:


get_ipython().system('mkdir skeletonimage/001')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/001 --display 0 --face --hand --write_images /content/skeletonimage/001  --disable_blending --alpha_pose 1  ')


# In[ ]:


os.chdir('/content/skeletonimage')


# In[ ]:


os.chdir('/content')


# In[ ]:


get_ipython().system('mkdir skeletonimage/002')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/002 --display 0 --face --hand --write_images /content/skeletonimage/002  --disable_blending --alpha_pose 1  ')


# In[ ]:


get_ipython().system('mkdir skeletonimages')


# In[ ]:


for i in range(1,10,1):
  print('!mkdir skeletonimages/00{}'.format(i))
  print('!cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/00{} --display 0 --face --hand --write_images /content/skeletonimages/00{}  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk00{}/ --part_candidates --model_pose BODY_25 '.format(i,i,i))  


# In[ ]:


for i in range(10,100,1):
  print('!mkdir skeletonimages/0{}'.format(i))
  print('!cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/0{} --display 0 --face --hand --write_images /content/skeletonimages/0{}  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk0{}/ --part_candidates --model_pose BODY_25 '.format(i,i,i))  


# In[ ]:


for i in range(100,202,1):
  print('!mkdir skeletonimages/{}'.format(i))
  print('!cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/{} --display 0 --face --hand --write_images /content/skeletonimages/{}  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk{}/ --part_candidates --model_pose BODY_25 '.format(i,i,i))  


# In[ ]:


get_ipython().system('mkdir skeletonimages/001')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/001 --display 0 --face --hand --write_images /content/skeletonimages/001  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk001/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/002')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/002 --display 0 --face --hand --write_images /content/skeletonimages/002  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk002/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/003')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/003 --display 0 --face --hand --write_images /content/skeletonimages/003  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk003/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/004')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/004 --display 0 --face --hand --write_images /content/skeletonimages/004  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk004/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/005')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/005 --display 0 --face --hand --write_images /content/skeletonimages/005  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk005/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/006')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/006 --display 0 --face --hand --write_images /content/skeletonimages/006  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk006/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/007')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/007 --display 0 --face --hand --write_images /content/skeletonimages/007  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk007/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/008')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/008 --display 0 --face --hand --write_images /content/skeletonimages/008  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk008/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/009')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/009 --display 0 --face --hand --write_images /content/skeletonimages/009  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk009/ --part_candidates --model_pose BODY_25 ')


# In[ ]:


get_ipython().system('mkdir skeletonimages/010')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/010 --display 0 --face --hand --write_images /content/skeletonimages/010  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk010/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/011')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/011 --display 0 --face --hand --write_images /content/skeletonimages/011  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk011/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/012')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/012 --display 0 --face --hand --write_images /content/skeletonimages/012  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk012/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/013')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/013 --display 0 --face --hand --write_images /content/skeletonimages/013  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk013/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/014')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/014 --display 0 --face --hand --write_images /content/skeletonimages/014  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk014/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/015')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/015 --display 0 --face --hand --write_images /content/skeletonimages/015  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk015/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/016')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/016 --display 0 --face --hand --write_images /content/skeletonimages/016  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk016/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/017')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/017 --display 0 --face --hand --write_images /content/skeletonimages/017  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk017/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/018')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/018 --display 0 --face --hand --write_images /content/skeletonimages/018  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk018/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/019')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/019 --display 0 --face --hand --write_images /content/skeletonimages/019  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk019/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/020')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/020 --display 0 --face --hand --write_images /content/skeletonimages/020  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk020/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/021')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/021 --display 0 --face --hand --write_images /content/skeletonimages/021  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk021/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/022')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/022 --display 0 --face --hand --write_images /content/skeletonimages/022  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk022/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/023')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/023 --display 0 --face --hand --write_images /content/skeletonimages/023  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk023/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/024')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/024 --display 0 --face --hand --write_images /content/skeletonimages/024  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk024/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/025')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/025 --display 0 --face --hand --write_images /content/skeletonimages/025  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk025/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/026')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/026 --display 0 --face --hand --write_images /content/skeletonimages/026  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk026/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/027')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/027 --display 0 --face --hand --write_images /content/skeletonimages/027  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk027/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/028')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/028 --display 0 --face --hand --write_images /content/skeletonimages/028  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk028/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/029')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/029 --display 0 --face --hand --write_images /content/skeletonimages/029  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk029/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/030')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/030 --display 0 --face --hand --write_images /content/skeletonimages/030  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk030/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/031')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/031 --display 0 --face --hand --write_images /content/skeletonimages/031  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk031/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/032')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/032 --display 0 --face --hand --write_images /content/skeletonimages/032  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk032/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/033')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/033 --display 0 --face --hand --write_images /content/skeletonimages/033  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk033/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/034')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/034 --display 0 --face --hand --write_images /content/skeletonimages/034  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk034/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/035')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/035 --display 0 --face --hand --write_images /content/skeletonimages/035  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk035/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/036')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/036 --display 0 --face --hand --write_images /content/skeletonimages/036  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk036/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/037')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/037 --display 0 --face --hand --write_images /content/skeletonimages/037  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk037/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/038')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/038 --display 0 --face --hand --write_images /content/skeletonimages/038  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk038/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/039')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/039 --display 0 --face --hand --write_images /content/skeletonimages/039  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk039/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/040')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/040 --display 0 --face --hand --write_images /content/skeletonimages/040  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk040/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/041')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/041 --display 0 --face --hand --write_images /content/skeletonimages/041  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk041/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/042')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/042 --display 0 --face --hand --write_images /content/skeletonimages/042  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk042/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/043')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/043 --display 0 --face --hand --write_images /content/skeletonimages/043  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk043/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/044')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/044 --display 0 --face --hand --write_images /content/skeletonimages/044  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk044/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/045')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/045 --display 0 --face --hand --write_images /content/skeletonimages/045  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk045/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/046')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/046 --display 0 --face --hand --write_images /content/skeletonimages/046  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk046/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/047')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/047 --display 0 --face --hand --write_images /content/skeletonimages/047  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk047/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/048')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/048 --display 0 --face --hand --write_images /content/skeletonimages/048  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk048/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/049')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/049 --display 0 --face --hand --write_images /content/skeletonimages/049  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk049/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/050')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/050 --display 0 --face --hand --write_images /content/skeletonimages/050  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk050/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/051')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/051 --display 0 --face --hand --write_images /content/skeletonimages/051  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk051/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/052')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/052 --display 0 --face --hand --write_images /content/skeletonimages/052  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk052/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/053')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/053 --display 0 --face --hand --write_images /content/skeletonimages/053  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk053/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/054')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/054 --display 0 --face --hand --write_images /content/skeletonimages/054  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk054/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/055')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/055 --display 0 --face --hand --write_images /content/skeletonimages/055  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk055/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/056')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/056 --display 0 --face --hand --write_images /content/skeletonimages/056  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk056/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/057')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/057 --display 0 --face --hand --write_images /content/skeletonimages/057  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk057/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/058')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/058 --display 0 --face --hand --write_images /content/skeletonimages/058  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk058/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/059')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/059 --display 0 --face --hand --write_images /content/skeletonimages/059  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk059/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/060')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/060 --display 0 --face --hand --write_images /content/skeletonimages/060  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk060/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/061')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/061 --display 0 --face --hand --write_images /content/skeletonimages/061  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk061/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/062')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/062 --display 0 --face --hand --write_images /content/skeletonimages/062  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk062/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/063')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/063 --display 0 --face --hand --write_images /content/skeletonimages/063  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk063/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/064')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/064 --display 0 --face --hand --write_images /content/skeletonimages/064  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk064/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/065')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/065 --display 0 --face --hand --write_images /content/skeletonimages/065  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk065/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/066')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/066 --display 0 --face --hand --write_images /content/skeletonimages/066  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk066/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/067')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/067 --display 0 --face --hand --write_images /content/skeletonimages/067  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk067/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/068')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/068 --display 0 --face --hand --write_images /content/skeletonimages/068  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk068/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/069')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/069 --display 0 --face --hand --write_images /content/skeletonimages/069  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk069/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/070')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/070 --display 0 --face --hand --write_images /content/skeletonimages/070  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk070/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/071')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/071 --display 0 --face --hand --write_images /content/skeletonimages/071  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk071/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/072')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/072 --display 0 --face --hand --write_images /content/skeletonimages/072  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk072/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/073')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/073 --display 0 --face --hand --write_images /content/skeletonimages/073  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk073/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/074')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/074 --display 0 --face --hand --write_images /content/skeletonimages/074  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk074/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/075')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/075 --display 0 --face --hand --write_images /content/skeletonimages/075  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk075/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/076')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/076 --display 0 --face --hand --write_images /content/skeletonimages/076  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk076/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/077')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/077 --display 0 --face --hand --write_images /content/skeletonimages/077  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk077/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/078')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/078 --display 0 --face --hand --write_images /content/skeletonimages/078  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk078/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/079')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/079 --display 0 --face --hand --write_images /content/skeletonimages/079  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk079/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/080')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/080 --display 0 --face --hand --write_images /content/skeletonimages/080  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk080/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/081')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/081 --display 0 --face --hand --write_images /content/skeletonimages/081  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk081/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/082')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/082 --display 0 --face --hand --write_images /content/skeletonimages/082  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk082/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/083')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/083 --display 0 --face --hand --write_images /content/skeletonimages/083  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk083/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/084')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/084 --display 0 --face --hand --write_images /content/skeletonimages/084  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk084/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/085')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/085 --display 0 --face --hand --write_images /content/skeletonimages/085  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk085/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/086')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/086 --display 0 --face --hand --write_images /content/skeletonimages/086  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk086/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/087')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/087 --display 0 --face --hand --write_images /content/skeletonimages/087  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk087/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/088')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/088 --display 0 --face --hand --write_images /content/skeletonimages/088  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk088/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/089')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/089 --display 0 --face --hand --write_images /content/skeletonimages/089  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk089/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/090')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/090 --display 0 --face --hand --write_images /content/skeletonimages/090  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk090/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/091')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/091 --display 0 --face --hand --write_images /content/skeletonimages/091  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk091/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/092')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/092 --display 0 --face --hand --write_images /content/skeletonimages/092  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk092/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/093')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/093 --display 0 --face --hand --write_images /content/skeletonimages/093  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk093/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/094')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/094 --display 0 --face --hand --write_images /content/skeletonimages/094  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk094/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/095')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/095 --display 0 --face --hand --write_images /content/skeletonimages/095  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk095/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/096')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/096 --display 0 --face --hand --write_images /content/skeletonimages/096  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk096/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/097')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/097 --display 0 --face --hand --write_images /content/skeletonimages/097  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk097/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/098')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/098 --display 0 --face --hand --write_images /content/skeletonimages/098  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk098/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/099')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/099 --display 0 --face --hand --write_images /content/skeletonimages/099  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk099/ --part_candidates --model_pose BODY_25 ')


# In[ ]:


for i in range(100,201,1):
  print('!mkdir skimages/{}'.format(i))
  print('!cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/{} --display 0 --face --hand --write_images /content/skimages/{}  --disable_blending --alpha_pose 1'.format(i,i))  


# In[ ]:


get_ipython().system('mkdir skeletonimages/100')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/100 --display 0 --face --hand --write_images /content/skeletonimages/100  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk100/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/101')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/101 --display 0 --face --hand --write_images /content/skeletonimages/101  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk101/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/102')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/102 --display 0 --face --hand --write_images /content/skeletonimages/102  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk102/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/103')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/103 --display 0 --face --hand --write_images /content/skeletonimages/103  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk103/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/104')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/104 --display 0 --face --hand --write_images /content/skeletonimages/104  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk104/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/105')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/105 --display 0 --face --hand --write_images /content/skeletonimages/105  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk105/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/106')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/106 --display 0 --face --hand --write_images /content/skeletonimages/106  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk106/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/107')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/107 --display 0 --face --hand --write_images /content/skeletonimages/107  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk107/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/108')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/108 --display 0 --face --hand --write_images /content/skeletonimages/108  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk108/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/109')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/109 --display 0 --face --hand --write_images /content/skeletonimages/109  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk109/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/110')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/110 --display 0 --face --hand --write_images /content/skeletonimages/110  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk110/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/111')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/111 --display 0 --face --hand --write_images /content/skeletonimages/111  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk111/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/112')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/112 --display 0 --face --hand --write_images /content/skeletonimages/112  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk112/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/113')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/113 --display 0 --face --hand --write_images /content/skeletonimages/113  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk113/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/114')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/114 --display 0 --face --hand --write_images /content/skeletonimages/114  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk114/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/115')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/115 --display 0 --face --hand --write_images /content/skeletonimages/115  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk115/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/116')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/116 --display 0 --face --hand --write_images /content/skeletonimages/116  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk116/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/117')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/117 --display 0 --face --hand --write_images /content/skeletonimages/117  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk117/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/118')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/118 --display 0 --face --hand --write_images /content/skeletonimages/118  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk118/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/119')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/119 --display 0 --face --hand --write_images /content/skeletonimages/119  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk119/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/120')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/120 --display 0 --face --hand --write_images /content/skeletonimages/120  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk120/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/121')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/121 --display 0 --face --hand --write_images /content/skeletonimages/121  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk121/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/122')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/122 --display 0 --face --hand --write_images /content/skeletonimages/122  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk122/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/123')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/123 --display 0 --face --hand --write_images /content/skeletonimages/123  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk123/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/124')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/124 --display 0 --face --hand --write_images /content/skeletonimages/124  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk124/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/125')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/125 --display 0 --face --hand --write_images /content/skeletonimages/125  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk125/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/126')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/126 --display 0 --face --hand --write_images /content/skeletonimages/126  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk126/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/127')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/127 --display 0 --face --hand --write_images /content/skeletonimages/127  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk127/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/128')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/128 --display 0 --face --hand --write_images /content/skeletonimages/128  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk128/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/129')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/129 --display 0 --face --hand --write_images /content/skeletonimages/129  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk129/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/130')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/130 --display 0 --face --hand --write_images /content/skeletonimages/130  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk130/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/131')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/131 --display 0 --face --hand --write_images /content/skeletonimages/131  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk131/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/132')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/132 --display 0 --face --hand --write_images /content/skeletonimages/132  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk132/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/133')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/133 --display 0 --face --hand --write_images /content/skeletonimages/133  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk133/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/134')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/134 --display 0 --face --hand --write_images /content/skeletonimages/134  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk134/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/135')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/135 --display 0 --face --hand --write_images /content/skeletonimages/135  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk135/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/136')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/136 --display 0 --face --hand --write_images /content/skeletonimages/136  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk136/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/137')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/137 --display 0 --face --hand --write_images /content/skeletonimages/137  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk137/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/138')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/138 --display 0 --face --hand --write_images /content/skeletonimages/138  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk138/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/139')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/139 --display 0 --face --hand --write_images /content/skeletonimages/139  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk139/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/140')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/140 --display 0 --face --hand --write_images /content/skeletonimages/140  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk140/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/141')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/141 --display 0 --face --hand --write_images /content/skeletonimages/141  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk141/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/142')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/142 --display 0 --face --hand --write_images /content/skeletonimages/142  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk142/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/143')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/143 --display 0 --face --hand --write_images /content/skeletonimages/143  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk143/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/144')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/144 --display 0 --face --hand --write_images /content/skeletonimages/144  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk144/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/145')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/145 --display 0 --face --hand --write_images /content/skeletonimages/145  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk145/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/146')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/146 --display 0 --face --hand --write_images /content/skeletonimages/146  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk146/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/147')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/147 --display 0 --face --hand --write_images /content/skeletonimages/147  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk147/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/148')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/148 --display 0 --face --hand --write_images /content/skeletonimages/148  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk148/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/149')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/149 --display 0 --face --hand --write_images /content/skeletonimages/149  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk149/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/150')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/150 --display 0 --face --hand --write_images /content/skeletonimages/150  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk150/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/151')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/151 --display 0 --face --hand --write_images /content/skeletonimages/151  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk151/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/152')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/152 --display 0 --face --hand --write_images /content/skeletonimages/152  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk152/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/153')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/153 --display 0 --face --hand --write_images /content/skeletonimages/153  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk153/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/154')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/154 --display 0 --face --hand --write_images /content/skeletonimages/154  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk154/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/155')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/155 --display 0 --face --hand --write_images /content/skeletonimages/155  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk155/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/156')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/156 --display 0 --face --hand --write_images /content/skeletonimages/156  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk156/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/157')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/157 --display 0 --face --hand --write_images /content/skeletonimages/157  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk157/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/158')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/158 --display 0 --face --hand --write_images /content/skeletonimages/158  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk158/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/159')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/159 --display 0 --face --hand --write_images /content/skeletonimages/159  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk159/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/160')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/160 --display 0 --face --hand --write_images /content/skeletonimages/160  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk160/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/161')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/161 --display 0 --face --hand --write_images /content/skeletonimages/161  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk161/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/162')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/162 --display 0 --face --hand --write_images /content/skeletonimages/162  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk162/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/163')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/163 --display 0 --face --hand --write_images /content/skeletonimages/163  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk163/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/164')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/164 --display 0 --face --hand --write_images /content/skeletonimages/164  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk164/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/165')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/165 --display 0 --face --hand --write_images /content/skeletonimages/165  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk165/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/166')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/166 --display 0 --face --hand --write_images /content/skeletonimages/166  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk166/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/167')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/167 --display 0 --face --hand --write_images /content/skeletonimages/167  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk167/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/168')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/168 --display 0 --face --hand --write_images /content/skeletonimages/168  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk168/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/169')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/169 --display 0 --face --hand --write_images /content/skeletonimages/169  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk169/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/170')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/170 --display 0 --face --hand --write_images /content/skeletonimages/170  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk170/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/171')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/171 --display 0 --face --hand --write_images /content/skeletonimages/171  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk171/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/172')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/172 --display 0 --face --hand --write_images /content/skeletonimages/172  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk172/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/173')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/173 --display 0 --face --hand --write_images /content/skeletonimages/173  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk173/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/174')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/174 --display 0 --face --hand --write_images /content/skeletonimages/174  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk174/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/175')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/175 --display 0 --face --hand --write_images /content/skeletonimages/175  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk175/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/176')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/176 --display 0 --face --hand --write_images /content/skeletonimages/176  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk176/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/177')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/177 --display 0 --face --hand --write_images /content/skeletonimages/177  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk177/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/178')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/178 --display 0 --face --hand --write_images /content/skeletonimages/178  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk178/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/179')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/179 --display 0 --face --hand --write_images /content/skeletonimages/179  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk179/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/180')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/180 --display 0 --face --hand --write_images /content/skeletonimages/180  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk180/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/181')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/181 --display 0 --face --hand --write_images /content/skeletonimages/181  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk181/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/182')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/182 --display 0 --face --hand --write_images /content/skeletonimages/182  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk182/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/183')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/183 --display 0 --face --hand --write_images /content/skeletonimages/183  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk183/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/184')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/184 --display 0 --face --hand --write_images /content/skeletonimages/184  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk184/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/185')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/185 --display 0 --face --hand --write_images /content/skeletonimages/185  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk185/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/186')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/186 --display 0 --face --hand --write_images /content/skeletonimages/186  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk186/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/187')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/187 --display 0 --face --hand --write_images /content/skeletonimages/187  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk187/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/188')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/188 --display 0 --face --hand --write_images /content/skeletonimages/188  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk188/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/189')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/189 --display 0 --face --hand --write_images /content/skeletonimages/189  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk189/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/190')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/190 --display 0 --face --hand --write_images /content/skeletonimages/190  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk190/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/191')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/191 --display 0 --face --hand --write_images /content/skeletonimages/191  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk191/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/192')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/192 --display 0 --face --hand --write_images /content/skeletonimages/192  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk192/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/193')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/193 --display 0 --face --hand --write_images /content/skeletonimages/193  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk193/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/194')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/194 --display 0 --face --hand --write_images /content/skeletonimages/194  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk194/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/195')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/195 --display 0 --face --hand --write_images /content/skeletonimages/195  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk195/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/196')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/196 --display 0 --face --hand --write_images /content/skeletonimages/196  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk196/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/197')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/197 --display 0 --face --hand --write_images /content/skeletonimages/197  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk197/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/198')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/198 --display 0 --face --hand --write_images /content/skeletonimages/198  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk198/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/199')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/199 --display 0 --face --hand --write_images /content/skeletonimages/199  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk199/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/200')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/200 --display 0 --face --hand --write_images /content/skeletonimages/200  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk200/ --part_candidates --model_pose BODY_25 ')
get_ipython().system('mkdir skeletonimages/201')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/201 --display 0 --face --hand --write_images /content/skeletonimages/201  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk201/ --part_candidates --model_pose BODY_25 ')


# In[ ]:


get_ipython().system('zip -r skeletonimages.zip skeletonimages')


# In[ ]:


# Install the PyDrive wrapper & import libraries.
# This only needs to be done once in a notebook.
get_ipython().system('pip install -U -q PyDrive')
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials
# Authenticate and create the PyDrive client.
# This only needs to be done once in a notebook.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)


# In[ ]:


# Create & upload a file.
uploaded = drive.CreateFile({'title': 'skeletonimages.zip'})
uploaded.SetContentFile('skeletonimages.zip')
uploaded.Upload()
print('Uploaded file with ID {}'.format(uploaded.get('id')))


# In[ ]:


import pandas as pd
import json


# In[ ]:


os.chdir('/content/skeletonimages/')


# In[ ]:


name='sk001/frame000000_cam0_keypoints.json'
with open(name) as datafile:
    data = json.load(datafile)


# In[ ]:


data['part_candidates'][0]['0']


# In[ ]:


for i in range(25):
  print("data{}=data['part_candidates'][0]['{}']".format(i,i))
  #print("datay{}=data['part_candidates'][0]['{}'][0]".format(i,i))


# In[ ]:


name='sk001/frame000000_cam0_keypoints.json'
with open(name) as datafile:
    data = json.load(datafile)


# In[ ]:


data0=np.array(data['part_candidates'][0]['0'])
data1=np.array(data['part_candidates'][0]['1'])
data2=np.array(data['part_candidates'][0]['2'])
data3=np.array(data['part_candidates'][0]['3'])
data4=np.array(data['part_candidates'][0]['4'])
data5=np.array(data['part_candidates'][0]['5'])
data6=np.array(data['part_candidates'][0]['6'])
data7=np.array(data['part_candidates'][0]['7'])
data8=np.array(data['part_candidates'][0]['8'])
data9=np.array(data['part_candidates'][0]['9'])
data10=np.array(data['part_candidates'][0]['10'])
data11=np.array(data['part_candidates'][0]['11'])
data12=np.array(data['part_candidates'][0]['12'])
data13=np.array(data['part_candidates'][0]['13'])
data14=np.array(data['part_candidates'][0]['14'])
data15=np.array(data['part_candidates'][0]['15'])
data16=np.array(data['part_candidates'][0]['16'])
data17=np.array(data['part_candidates'][0]['17'])
data18=np.array(data['part_candidates'][0]['18'])
data19=np.array(data['part_candidates'][0]['19'])
data20=np.array(data['part_candidates'][0]['20'])
data21=np.array(data['part_candidates'][0]['21'])
data22=np.array(data['part_candidates'][0]['22'])
data23=np.array(data['part_candidates'][0]['23'])
data24=np.array(data['part_candidates'][0]['24'])
data25=data['people'][0]['face_keypoints_2d']
data26=data['people'][0]['hand_left_keypoints_2d']
data27=data['people'][0]['hand_right_keypoints_2d']
data28=data['people'][0]['pose_keypoints_2d']                  


# In[ ]:


d = { 'name':name,             'pos0': data0,
'pos1': data1,
'pos2': data2,
'pos3': data3,
'pos4': data4,
'pos5': data5,
'pos6': data6,
'pos7': data7,
'pos8': data8,
'pos9': data9,
'pos10': data10,
'pos11': data11,
'pos12': data12,
'pos13': data13,
'pos14': data14,
'pos15': data15,
'pos16': data16,
'pos17': data17,
'pos18': data18,
'pos19': data19,
'pos20': data20,
'pos21': data21,
'pos22': data22,
'pos23': data23,
'pos24': data24,
}
df = pd.DataFrame.from_dict(data=d,orient='index')
df=df.transpose()
bodyname='body.csv'
df.to_csv(bodyname)


d1={'name':name,'pos25': data25
 }
df1 = pd.DataFrame.from_dict(data=d1,orient='index')
df1=df1.transpose()
facedetail='face.csv'
df1.to_csv(facedetail)

d2={'name':name,
'pos26': data26,
'pos27': data27
 }
df2 = pd.DataFrame.from_dict(data=d2,orient='index')
df2=df2.transpose()
handsdetail='leftandrighthands.csv'
df2.to_csv(handsdetail)

d3={'name':name,
'pos28': data28
 }
df3 = pd.DataFrame.from_dict(data=d3,orient='index')
df3=df3.transpose()
facedetail='face.csv'
df3.to_csv(facedetail)


# In[ ]:


name='sk005/frame000000_cam0_keypoints.json'
s=name.split('/')[0]
se=s.split('k')[1]
ss=name.split('/')[1]
sss=ss.split('_')
se+'/'+sss[0]+'_'+sss[1]+"_"+"rendered.png"


# In[ ]:


fol=[]
for i in range(1,10,1):
  fol.append("sk00{}".format(i))
for i in range(10,100,1):
  fol.append("sk0{}".format(i))
for i in range(100,202,1):
  fol.append("sk{}".format(i))
fol


# In[ ]:


os.chdir('/content/skeletonimages/')


# In[ ]:


for i in fol:
  #print(i+'/')
  n=sorted(os.listdir(i+'/'))
  for n in n:
    #name='sk005/frame000000_cam0_keypoints.json'
    name=i+'/'+n
    print(name)
    with open(name) as datafile:
        data = json.load(datafile)
    s=name.split('/')[0]
    se=s.split('k')[1]
    ss=name.split('/')[1]
    sss=ss.split('_')
    nam=se+'/'+sss[0]+'_'+sss[1]+"_"+"rendered.png"
    data0=data['part_candidates'][0]['0']
    data1=data['part_candidates'][0]['1']
    data2=data['part_candidates'][0]['2']
    data3=data['part_candidates'][0]['3']
    data4=data['part_candidates'][0]['4']
    data5=data['part_candidates'][0]['5']
    data6=data['part_candidates'][0]['6']
    data7=data['part_candidates'][0]['7']
    data8=data['part_candidates'][0]['8']
    data9=data['part_candidates'][0]['9']
    data10=data['part_candidates'][0]['10']
    data11=data['part_candidates'][0]['11']
    data12=data['part_candidates'][0]['12']
    data13=data['part_candidates'][0]['13']
    data14=data['part_candidates'][0]['14']
    data15=data['part_candidates'][0]['15']
    data16=data['part_candidates'][0]['16']
    data17=data['part_candidates'][0]['17']
    data18=data['part_candidates'][0]['18']
    data19=data['part_candidates'][0]['19']
    data20=data['part_candidates'][0]['20']
    data21=data['part_candidates'][0]['21']
    data22=data['part_candidates'][0]['22']
    data23=data['part_candidates'][0]['23']
    data24=data['part_candidates'][0]['24']
    data25=data['people'][0]['face_keypoints_2d']
    data26=data['people'][0]['hand_left_keypoints_2d']
    data27=data['people'][0]['hand_right_keypoints_2d']
    data28=data['people'][0]['pose_keypoints_2d']                  



    d = { 'name':nam,             'pos0': data0,
    'pos1': data1,
    'pos2': data2,
    'pos3': data3,
    'pos4': data4,
    'pos5': data5,
    'pos6': data6,
    'pos7': data7,
    'pos8': data8,
    'pos9': data9,
    'pos10': data10,
    'pos11': data11,
    'pos12': data12,
    'pos13': data13,
    'pos14': data14,
    'pos15': data15,
    'pos16': data16,
    'pos17': data17,
    'pos18': data18,
    'pos19': data19,
    'pos20': data20,
    'pos21': data21,
    'pos22': data22,
    'pos23': data23,
    'pos24': data24,
    'pos25': data25,
    'pos26': data26,
    'pos27': data27,
    'pos28': data28,
    }
    df = pd.DataFrame.from_dict(data=d,orient='index')
    df=df.transpose()
    #bodyname='body.csv'
    #df.to_csv(bodyname)

    with open('finalbody.csv', 'a') as f:
        df.to_csv(f,header=False)


# In[ ]:


name='sk002/frame000000_cam0_keypoints.json'
with open(name) as datafile:
    data = json.load(datafile)

data0=np.array(data['part_candidates'][0]['0'])
data1=np.array(data['part_candidates'][0]['1'])
data2=np.array(data['part_candidates'][0]['2'])
data3=np.array(data['part_candidates'][0]['3'])
data4=np.array(data['part_candidates'][0]['4'])
data5=np.array(data['part_candidates'][0]['5'])
data6=np.array(data['part_candidates'][0]['6'])
data7=np.array(data['part_candidates'][0]['7'])
data8=np.array(data['part_candidates'][0]['8'])
data9=np.array(data['part_candidates'][0]['9'])
data10=np.array(data['part_candidates'][0]['10'])
data11=np.array(data['part_candidates'][0]['11'])
data12=np.array(data['part_candidates'][0]['12'])
data13=np.array(data['part_candidates'][0]['13'])
data14=np.array(data['part_candidates'][0]['14'])
data15=np.array(data['part_candidates'][0]['15'])
data16=np.array(data['part_candidates'][0]['16'])
data17=np.array(data['part_candidates'][0]['17'])
data18=np.array(data['part_candidates'][0]['18'])
data19=np.array(data['part_candidates'][0]['19'])
data20=np.array(data['part_candidates'][0]['20'])
data21=np.array(data['part_candidates'][0]['21'])
data22=np.array(data['part_candidates'][0]['22'])
data23=np.array(data['part_candidates'][0]['23'])
data24=np.array(data['part_candidates'][0]['24'])   
    
    
    
    
d = {name,             data0,
      data1,
      data2,
      data3,
      data4,
      data5,
      data6,
      data7,
      data8,
      data9,
      data10,
      data11,
      data12,
      data13,
      data14,
      data15,
      data16,
      data17,
      data18,
      data19,
      data20,
      data21,
      data22,
      data23,
      data24}

df = pd.DataFrame.from_dict(data=d,orient='index')
df=df.transpose()
bodyname='body.csv'
df.to_csv(bodyname)

with open('body.csv', 'a') as f:
    df.to_csv(df,header=False)


# In[ ]:


for i in range(25):
  print("data{},".format(i))


# In[ ]:


df.head()


# In[ ]:


os.chdir('/content')


# In[ ]:


get_ipython().system('mkdir skeletonimages/001')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/001 --display 0 --face --hand --write_images /content/skeletonimages/001  --disable_blending --alpha_pose 1 --write_json /content/skeletonimages/sk001/ --part_candidates --model_pose BODY_25')


# In[ ]:


import shutil
shutil.rmtree('/content/skeletonimages/sk001')


# In[ ]:


import os
d=os.listdir('/content/skeletonimages')
len(d)


# In[ ]:



get_ipython().system('zip -r sk.zip skeletonimages')


# In[ ]:


get_ipython().system('zip -r skjson.zip skeletonjson')


# In[ ]:




