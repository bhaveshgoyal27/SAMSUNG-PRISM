from skimage.measure import regionprops
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('test.png')

segments = slic(image, n_segments = 50, sigma = 5)
img=mark_boundaries(image, segments)
cv2.imshow("bhvb",img)
l=[]
regions = regionprops(segments)
for props in regions:
    cx, cy = props.centroid
    a=int(cx)
    b=int(cy)
    l.append([a,b])
    cv2.circle(img,(a,b),1,(0,0,255),-1)
    img[a,b]=[0,0,255]

cv2.imshow("bhvh",img)
print(len(l))
cv2.waitKey(0)
cv2.destroyAllWindows()
