#!/usr/bin/env python
# coding: utf-8

# # Pose Detection with OpenPose
# 
# This notebook uses an open source project [CMU-Perceptual-Computing-Lab/openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose.git) to detect/track multi person poses on a given youtube video.
# 
# For other deep-learning Colab notebooks, visit [tugstugi/dl-colab-notebooks](https://github.com/tugstugi/dl-colab-notebooks).
# 
# 
# ## Install OpenPose

# In[ ]:


get_ipython().system('git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git')


# In[ ]:


import os
from os.path import exists, join, basename, splitext

git_repo_url = 'https://github.com/CMU-Perceptual-Computing-Lab/openpose.git'
project_name = splitext(basename(git_repo_url))[0]
if  exists(project_name):
  # see: https://github.com/CMU-Perceptual-Computing-Lab/openpose/issues/949
  # install new CMake becaue of CUDA10
  get_ipython().system('wget -q https://cmake.org/files/v3.13/cmake-3.13.0-Linux-x86_64.tar.gz')
  get_ipython().system('tar xfz cmake-3.13.0-Linux-x86_64.tar.gz --strip-components=1 -C /usr/local')
  # clone openpose
  get_ipython().system('git clone -q --depth 1 $git_repo_url')
  get_ipython().system("sed -i 's/execute_process(COMMAND git checkout master WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\\/3rdparty\\/caffe)/execute_process(COMMAND git checkout f019d0dfe86f49d1140961f8c7dec22130c83154 WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}\\/3rdparty\\/caffe)/g' openpose/CMakeLists.txt")
  # install system dependencies
  get_ipython().system('apt-get -qq install -y libatlas-base-dev libprotobuf-dev libleveldb-dev libsnappy-dev libhdf5-serial-dev protobuf-compiler libgflags-dev libgoogle-glog-dev liblmdb-dev opencl-headers ocl-icd-opencl-dev libviennacl-dev')
  # install python dependencies
  get_ipython().system('pip install -q youtube-dl')
  # build openpose
  get_ipython().system('cd openpose && rm -rf build || true && mkdir build && cd build && cmake .. && make -j`nproc`')
  
from IPython.display import YouTubeVideo


# ## Detect poses on a test video
# 
# We are going to detect poses on the following youtube video:

# In[ ]:


YOUTUBE_ID = 'RXABo9hm8B8'


YouTubeVideo(YOUTUBE_ID)


# Download the above youtube video, cut the first 5 seconds and do the pose detection on that 5 seconds:

# In[ ]:


get_ipython().system('rm -rf youtube.mp4')
# download the youtube with the given ID
get_ipython().system('youtube-dl -f \'bestvideo[ext=mp4]\' --output "youtube.%(ext)s" https://www.youtube.com/watch?v=$YOUTUBE_ID')
# cut the first 5 seconds
get_ipython().system('ffmpeg -y -loglevel info -i youtube.mp4 -t 5 video.mp4')
# detect poses on the these 5 seconds
get_ipython().system('rm openpose.avi')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --video ../video.mp4 --write_json ./output/ --display 0 --face --hand --write_video ../openpose.avi')
# convert the result into MP4
get_ipython().system('ffmpeg -y -loglevel info -i openpose.avi output.mp4')


# In[ ]:


get_ipython().system('ffmpeg -y -loglevel info -i youtube.mp4 -t 10 video.mp4')
# detect poses on the these 5 seconds
get_ipython().system('rm openpose.avi')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --video ../video.mp4 --write_json ./output/ --display 0 --render_pose 0 --face --face_render 2 --hand --hand_render 2 --write_video ../openpose.avi')
# convert the result into MP4
get_ipython().system('ffmpeg -y -loglevel info -i openpose.avi output.mp4')


# Finally, visualize the result:

# In[ ]:


def show_local_mp4_video(file_name, width=640, height=480):
  import io
  import base64
  from IPython.display import HTML
  video_encoded = base64.b64encode(io.open(file_name, 'rb').read())
  return HTML(data='''<video width="{0}" height="{1}" alt="test" controls>
                        <source src="data:video/mp4;base64,{2}" type="video/mp4" />
                      </video>'''.format(width, height, video_encoded.decode('ascii')))

show_local_mp4_video('output.mp4', width=960, height=720)


# In[ ]:


path='/content/rwth-boston-104/videoBank/camera0/001_0.mpg'
get_ipython().system('ffmpeg -y -loglevel info -i /content/rwth-boston-104/videoBank/camera0/001_0.mpg -t 5 videos.mp4')
#!ffmpeg -y -loglevel info -i youtube.mp4 -t 10 video.mp4


# In[ ]:


get_ipython().system('rm openpose.avi')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --video ../videos.mp4 --write_json ./output/ --display 0 --face --hand --write_video ../signs.avi')
# convert the result into MP4
get_ipython().system('ffmpeg -y -loglevel info -i sign.avi language.mp4')


# In[ ]:


def show_local_mp4_video(file_name, width=640, height=480):
  import io
  import base64
  from IPython.display import HTML
  video_encoded = base64.b64encode(io.open(file_name, 'rb').read())
  return HTML(data='''<video width="{0}" height="{1}" alt="test" controls>
                        <source src="data:video/mp4;base64,{2}" type="video/mp4" />
                      </video>'''.format(width, height, video_encoded.decode('ascii')))

show_local_mp4_video('language.mp4', width=960, height=720)


# In[ ]:


get_ipython().system('rm openpose.avi')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --video ../videos.mp4 --write_json ./output/  --write_video ../signss.avi --disable_blending  --alpha_pose 1')
# convert the result into MP4


# In[ ]:


def show_local_mp4_video(file_name, width=640, height=480):
  import io
  import base64
  from IPython.display import HTML
  video_encoded = base64.b64encode(io.open(file_name, 'rb').read())
  return HTML(data='''<video width="{0}" height="{1}" alt="test" controls>
                        <source src="data:video/mp4;base64,{2}" type="video/mp4" />
                      </video>'''.format(width, height, video_encoded.decode('ascii')))

show_local_mp4_video('language.mp4', width=960, height=720)


# In[ ]:


get_ipython().system('mkdir heatmaps')


# In[ ]:


get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --video ../videos.mp4  --display 0 --face --hand --write_video ../output.avi --disable_blending --alpha_pose 1')


# In[ ]:


get_ipython().system('ffmpeg -y -loglevel info -i output.avi  languages.mp4')


# In[ ]:





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


for i in range(10,99,1):
  print('!mkdir skimages/0{}'.format(i))
  print('!cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/0{} --display 0 --face --hand --write_images /content/skimages/0{}  --disable_blending --alpha_pose 1'.format(i,i))  


# In[ ]:


get_ipython().system('mkdir skimages/010')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/010 --display 0 --face --hand --write_images /content/skimages/010  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/011')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/011 --display 0 --face --hand --write_images /content/skimages/011  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/012')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/012 --display 0 --face --hand --write_images /content/skimages/012  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/013')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/013 --display 0 --face --hand --write_images /content/skimages/013  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/014')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/014 --display 0 --face --hand --write_images /content/skimages/014  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/015')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/015 --display 0 --face --hand --write_images /content/skimages/015  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/016')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/016 --display 0 --face --hand --write_images /content/skimages/016  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/017')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/017 --display 0 --face --hand --write_images /content/skimages/017  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/018')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/018 --display 0 --face --hand --write_images /content/skimages/018  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/019')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/019 --display 0 --face --hand --write_images /content/skimages/019  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/020')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/020 --display 0 --face --hand --write_images /content/skimages/020  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/021')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/021 --display 0 --face --hand --write_images /content/skimages/021  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/022')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/022 --display 0 --face --hand --write_images /content/skimages/022  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/023')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/023 --display 0 --face --hand --write_images /content/skimages/023  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/024')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/024 --display 0 --face --hand --write_images /content/skimages/024  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/025')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/025 --display 0 --face --hand --write_images /content/skimages/025  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/026')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/026 --display 0 --face --hand --write_images /content/skimages/026  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/027')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/027 --display 0 --face --hand --write_images /content/skimages/027  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/028')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/028 --display 0 --face --hand --write_images /content/skimages/028  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/029')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/029 --display 0 --face --hand --write_images /content/skimages/029  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/030')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/030 --display 0 --face --hand --write_images /content/skimages/030  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/031')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/031 --display 0 --face --hand --write_images /content/skimages/031  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/032')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/032 --display 0 --face --hand --write_images /content/skimages/032  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/033')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/033 --display 0 --face --hand --write_images /content/skimages/033  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/034')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/034 --display 0 --face --hand --write_images /content/skimages/034  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/035')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/035 --display 0 --face --hand --write_images /content/skimages/035  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/036')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/036 --display 0 --face --hand --write_images /content/skimages/036  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/037')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/037 --display 0 --face --hand --write_images /content/skimages/037  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/038')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/038 --display 0 --face --hand --write_images /content/skimages/038  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/039')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/039 --display 0 --face --hand --write_images /content/skimages/039  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/040')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/040 --display 0 --face --hand --write_images /content/skimages/040  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/041')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/041 --display 0 --face --hand --write_images /content/skimages/041  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/042')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/042 --display 0 --face --hand --write_images /content/skimages/042  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/043')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/043 --display 0 --face --hand --write_images /content/skimages/043  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/044')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/044 --display 0 --face --hand --write_images /content/skimages/044  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/045')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/045 --display 0 --face --hand --write_images /content/skimages/045  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/046')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/046 --display 0 --face --hand --write_images /content/skimages/046  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/047')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/047 --display 0 --face --hand --write_images /content/skimages/047  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/048')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/048 --display 0 --face --hand --write_images /content/skimages/048  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/049')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/049 --display 0 --face --hand --write_images /content/skimages/049  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/050')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/050 --display 0 --face --hand --write_images /content/skimages/050  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/051')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/051 --display 0 --face --hand --write_images /content/skimages/051  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/052')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/052 --display 0 --face --hand --write_images /content/skimages/052  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/053')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/053 --display 0 --face --hand --write_images /content/skimages/053  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/054')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/054 --display 0 --face --hand --write_images /content/skimages/054  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/055')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/055 --display 0 --face --hand --write_images /content/skimages/055  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/056')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/056 --display 0 --face --hand --write_images /content/skimages/056  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/057')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/057 --display 0 --face --hand --write_images /content/skimages/057  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/058')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/058 --display 0 --face --hand --write_images /content/skimages/058  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/059')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/059 --display 0 --face --hand --write_images /content/skimages/059  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/060')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/060 --display 0 --face --hand --write_images /content/skimages/060  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/061')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/061 --display 0 --face --hand --write_images /content/skimages/061  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/062')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/062 --display 0 --face --hand --write_images /content/skimages/062  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/063')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/063 --display 0 --face --hand --write_images /content/skimages/063  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/064')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/064 --display 0 --face --hand --write_images /content/skimages/064  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/065')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/065 --display 0 --face --hand --write_images /content/skimages/065  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/066')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/066 --display 0 --face --hand --write_images /content/skimages/066  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/067')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/067 --display 0 --face --hand --write_images /content/skimages/067  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/068')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/068 --display 0 --face --hand --write_images /content/skimages/068  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/069')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/069 --display 0 --face --hand --write_images /content/skimages/069  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/070')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/070 --display 0 --face --hand --write_images /content/skimages/070  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/071')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/071 --display 0 --face --hand --write_images /content/skimages/071  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/072')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/072 --display 0 --face --hand --write_images /content/skimages/072  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/073')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/073 --display 0 --face --hand --write_images /content/skimages/073  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/074')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/074 --display 0 --face --hand --write_images /content/skimages/074  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/075')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/075 --display 0 --face --hand --write_images /content/skimages/075  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/076')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/076 --display 0 --face --hand --write_images /content/skimages/076  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/077')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/077 --display 0 --face --hand --write_images /content/skimages/077  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/078')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/078 --display 0 --face --hand --write_images /content/skimages/078  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/079')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/079 --display 0 --face --hand --write_images /content/skimages/079  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/080')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/080 --display 0 --face --hand --write_images /content/skimages/080  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/081')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/081 --display 0 --face --hand --write_images /content/skimages/081  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/082')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/082 --display 0 --face --hand --write_images /content/skimages/082  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/083')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/083 --display 0 --face --hand --write_images /content/skimages/083  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/084')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/084 --display 0 --face --hand --write_images /content/skimages/084  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/085')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/085 --display 0 --face --hand --write_images /content/skimages/085  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/086')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/086 --display 0 --face --hand --write_images /content/skimages/086  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/087')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/087 --display 0 --face --hand --write_images /content/skimages/087  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/088')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/088 --display 0 --face --hand --write_images /content/skimages/088  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/089')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/089 --display 0 --face --hand --write_images /content/skimages/089  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/090')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/090 --display 0 --face --hand --write_images /content/skimages/090  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/091')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/091 --display 0 --face --hand --write_images /content/skimages/091  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/092')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/092 --display 0 --face --hand --write_images /content/skimages/092  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/093')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/093 --display 0 --face --hand --write_images /content/skimages/093  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/094')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/094 --display 0 --face --hand --write_images /content/skimages/094  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/095')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/095 --display 0 --face --hand --write_images /content/skimages/095  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/096')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/096 --display 0 --face --hand --write_images /content/skimages/096  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/097')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/097 --display 0 --face --hand --write_images /content/skimages/097  --disable_blending --alpha_pose 1')
get_ipython().system('mkdir skimages/098')
get_ipython().system('cd openpose && ./build/examples/openpose/openpose.bin --image_dir /content/data/png-segments/098 --display 0 --face --hand --write_images /content/skimages/098  --disable_blending --alpha_pose 1')


# In[ ]:


# import the OpenCV package
import cv2

# load the image with imread()
imageSource = '/content/vedio/frame0.jpg'
img = cv2.imread(imageSource)

# copy image to display all 4 variations
horizontal_img = img
vertical_img = img
both_img = img

# flip img horizontally, vertically,
# and both axes with flip()
horizontal_img = cv2.flip( img, 0 )
vertical_img = cv2.flip( img, 1 )
both_img = cv2.flip( img, -1 )

# display the images on screen with imshow()
#cv2.imshow( "Original", img )
import matplotlib.pyplot as plt
cv2.imwrite( "Horizontalfl.png", both_img )


# In[ ]:


get_ipython().system('ffmpeg -y -loglevel info -i output.avi  output.mp4')


# In[ ]:


cd pix2pix-tensorflow


# In[ ]:


get_ipython().system('mkdir results2')


# In[ ]:


get_ipython().system('python pix2pix.py   --mode test   --output_dir results2   --input_dir /content/f/test   --checkpoint /content/trainl')


# In[ ]:


get_ipython().system('zip -r results2.zip results2')


# In[ ]:




