import cv2
import os
import numpy as np

flash=cv2.imread("./Objects_007_flash.png",0)
amb=cv2.imread("./Objects_007_ambient.png")
flash=cv2.resize(flash,(512,512),interpolation=cv2.INTER_AREA)
amb=cv2.resize(amb,(512,512),interpolation=cv2.INTER_AREA)

"""
hsvf=cv2.cvtColor(flash,cv2.COLOR_BGR2HSV)
hsva=cv2.cvtColor(amb,cv2.COLOR_BGR2HSV)

hf,sf,vf=cv2.split(hsvf)
ha,sa,va=cv2.split(hsva)

cv2.imshow("hf",hf)
cv2.imshow("sf",sf)
cv2.imshow("vf",vf)
cv2.imshow("ha",ha)
cv2.imshow("sa",sa)
cv2.imshow("va",va)
"""

"""
#cv2.imshow("vf",vf)
#cv2.imshow("va",va)
su=cv2.subtract(sf,sa)
#cv2.imshow("su",su)
hsvf[:,:,0]=ha
#Shsvf[:,:,1]=sa
f=cv2.cvtColor(hsvf,cv2.COLOR_HSV2BGR)
cv2.imshow("removal",f)
cv2.imshow("flash",flash)
cv2.imshow("amb",amb)
cv2.WaitKeys(0)
cv2.destroyAllWindow()
"""

ret2,th2 = cv2.threshold(flash,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
a=flash<ret2
b=flash>ret2
i=np.zeros((512,512,1))
j=np.zeros((512,512,1))
i[:,:,0]=a
j[:,:,0]=b
cv2.imshow("bg",i)
cv2.imshow("fg",j)

