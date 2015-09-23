from skimage.io import imread
from skimage.transform import resize
from matplotlib import pyplot as plt
import matplotlib.cm as cm

example_file = ("http://upload.wikimedia.org/"+"wikipedia/commons/7/7d/Dog_face.png")
image=imread(example_file, as_grey=True)                   #Read the image into memory 
#plt.imshow(image, cmap=cm.gray)
image2=image[5:70,0:70]                              #Crop the image 
image3=resize (image2, (30,30),mode='nearest')        #Change the image to 30/30 pixel from 90/90 pixel 
plt.imshow(image3, cmap=cm.gray)                            
plt.show()
image_row=image3.flatten()                             #Flatten the picture data from 30/30 array to single dimension 900 elements stored in image_row
print("data type: %s, shape: %s" % (type(image3), image3.shape))            
print("data type: %s, shape: %s" % (type(image_row), image_row.shape))


