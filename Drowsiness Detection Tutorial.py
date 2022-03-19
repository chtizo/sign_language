


import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2


# In[ ]:

 #pip list |findstr opencv
#get_ipython().system('pip install opencv-python-headless<4.3')


# # 2. Load Model

# In[2]:


model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


# In[3]:


#model


# # 3. Make Detections with Images

# In[4]:


##img = 'https://raw.githubusercontent.com/ultralytics/yolov5/master/data/images/zidane.jpg'


# In[5]:


#results = model(img)
#print(results.print())


# In[6]:


#get_ipython().run_line_magic('matplotlib', 'inline')
#plt.imshow(np.squeeze(results.render()))
#plt.show()


# In[7]:


#results.render()


# # 4. Real Time Detections

# In[13]:


##cap = cv2.VideoCapture(0)
##while cap.isOpened():
##    ret, frame = cap.read()
##    
##    # Make detections 
##    results = model(frame)
##    
##    cv2.imshow('YOLO', np.squeeze(results.render()))
##    
##    if cv2.waitKey(10) & 0xFF == ord('q'):
##        break
##cap.release()
##cv2.destroyAllWindows()


### # 5. Train from scratch
##
### In[14]:
##
##
import uuid   # Unique identifier
import os
import time
##
##
### In[15]:
##
##
IMAGES_PATH = os.path.join('data', 'images') #/data/images
labels = ['awake', 'drowsy']
##number_imgs = 20
##
##
### In[16]:
##
##
##cap = cv2.VideoCapture(0)
### Loop through labels
##for label in labels:
##    print('Collecting images for {}'.format(label))
##    time.sleep(5)
##    
##    # Loop through image range
##    for img_num in range(number_imgs):
##        print('Collecting images for {}, image number {}'.format(label, img_num))
##        
##        # Webcam feed
##        ret, frame = cap.read()
##        
##        # Naming out image path
##        imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')
##        cv2.putText(frame, '{}'.format(img_num), (50,200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)
##        # Writes out image to file 
##        cv2.imwrite(imgname, frame)
##        
##        # Render to the screen
##        cv2.imshow('Image Collection', frame)
##        
##        # 2 second delay between captures
##        time.sleep(2)
##        
##        if cv2.waitKey(10) & 0xFF == ord('q'):
##            break
##cap.release()
##cv2.destroyAllWindows()
##
##
### In[ ]:
##
##
##print(os.path.join(IMAGES_PATH, labels[0]+'.'+str(uuid.uuid1())+'.jpg'))
##
##
### In[ ]:
##
##
##for label in labels:
##    print('Collecting images for {}'.format(label))
##    for img_num in range(number_imgs):
##        print('Collecting images for {}, image number {}'.format(label, img_num))
##        imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')
##        print(imgname)   
##
##
### In[ ]:
##
##
##get_ipython().system('git clone https://github.com/tzutalin/labelImg')
##
##
### In[ ]:
##
##
##get_ipython().system('pip install pyqt5 lxml --upgrade //streamlit')
##get_ipython().system('cd labelImg && pyrcc5 -o libs/resources.py resources.qrc')
##
##
### In[ ]:
##
##
##get_ipython().system('cd yolov5 && python train.py --img 320 --batch 1 --epochs 500 --data dataset.yml --weights yolov5s.pt --workers 2')
##
##
### # 6. Load Custom Model
##
### In[ ]:
##
##
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp12/weights/last.pt', force_reload=True)
##
##
### In[ ]:
##
##
img = os.path.join('data', 'images', 'drowsy.18ac8d00-80e7-11ec-8247-5c879c719f9a.jpg')
##
##
### In[ ]:
##
##
results = model(img)
##
##
### In[ ]:
##
##
print(results.render()[0])
##
##
### In[ ]:
##
##
##get_ipython().run_line_magic('matplotlib', 'inline')
##plt.imshow(np.squeeze(results.render())) 
##plt.show()
##
##
### In[ ]:
##
##
##cap = cv2.VideoCapture(0)
##while cap.isOpened():
##    ret, frame = cap.read()
##    
##    # Make detections 
##    results = model(frame)
##    
##    cv2.imshow('YOLO', np.squeeze(results.render()))
##    
##    if cv2.waitKey(10) & 0xFF == ord('q'):
##        break
##cap.release()
##cv2.destroyAllWindows()
##
##
### In[ ]:
##



