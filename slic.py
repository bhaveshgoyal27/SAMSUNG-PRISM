from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import cv2
import matplotlib.pyplot as plt
image = cv2.imread('test.png')

"""
for numSegments in (100, 200, 300):
	segments = slic(image, n_segments = numSegments, sigma = 5)
	fig = plt.figure("Superpixels -- %d segments" % (numSegments))
	ax = fig.add_subplot(1, 1, 1)
	ax.imshow(mark_boundaries(image, segments))
	plt.axis("off")
plt.show()
"""
numSegments=5
segments = slic(image, n_segments = numSegments, sigma = 5)
fig = plt.figure("Superpixels -- %d segments" % (numSegments))
cv2.imshow("jhb",mark_boundaries(image, segments))
