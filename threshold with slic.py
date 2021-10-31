import cv2
import numpy as np
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries

img=cv2.imread('Objects_005_flash.png')
img1=cv2.imread('Objects_005_ambient.png')
dim=(512,512)
img=cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
img1=cv2.resize(img1, dim, interpolation = cv2.INTER_AREA)

"""
_,img1 = cv2.threshold(img,75,255,cv2.THRESH_TOZERO)
cv2.imshow("f",img)
cv2.imshow("chg",img1)
numSegments=50
segments = slic(img1, n_segments = numSegments, sigma = 5)
cv2.imshow("jhb",mark_boundaries(img1, segments))
"""

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
_, inv1 = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY_INV)
_, inv = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)


"""
contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
cv2.imshow('original',img)
print("Number of contours="+str(len(contours)))
cv2.drawContours(img,contours,-1,(255,0,255),1)

cv2.imshow('contours',img)
cv2.imshow('threshold',threshold)
"""

img2=np.zeros_like(img)
img2[:,:,0]=inv
img2[:,:,1]=inv
img2[:,:,2]=inv

img3=np.zeros_like(img)
img3[:,:,0]=inv1
img3[:,:,1]=inv1
img3[:,:,2]=inv1

inv1=cv2.bitwise_and(img3,img1)
inv=cv2.bitwise_and(img2,img)

i=cv2.bitwise_or(inv1,inv)
"""
cv2.imshow("non-flash",inv1)
cv2.imshow("flash",inv)
"""
cv2.imshow("yfgjh",i)
cv2.waitKey(0)
cv2.destroyAllWindows()
