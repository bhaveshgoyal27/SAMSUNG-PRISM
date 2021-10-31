import cv2
import numpy as np
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries

img=cv2.imread('Objects_005_ambient.png')
img1=cv2.imread('Objects_005_flash.png')
dim=(512,512)
img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img1=cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)


gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
retval1, mask1 = cv2.threshold(gray1, 90, 255, cv2.THRESH_BINARY)

mask=np.zeros((512,512,3),dtype="uint8")
mask[:,:,0]=mask1
mask[:,:,1]=mask1
mask[:,:,2]=mask1

gen1=cv2.bitwise_or(mask,img1)
gen=cv2.bitwise_or(mask,img)

cv2.imshow("flasgen",gen1)
cv2.imshow("ambgen",gen)
