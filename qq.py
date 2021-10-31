import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_mask(mask, image, title='', mask_color=(255, 255, 255)):
    display_image = image.copy()
    display_image[mask != 0] = mask_color
    plt.imshow(display_image)
    plt.title(title)
    plt.axis('off')
    plt.show()


def compute_otsu_mask_shadows(image, shadow_percentile=5):
    image_hls = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)

    hue, lightness, saturation = np.split(image_hls, 3, axis=2)
    hue = hue.reshape((hue.shape[0], hue.shape[1]))

    otsu = cv2.threshold(hue, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    otsu_mask = otsu != 255

    image_lab = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    l, a, b = np.split(image_lab, 3, axis=2)
    l = l.reshape((l.shape[0], l.shape[1]))

    shadow_threshold = np.percentile(l.ravel(), q=shadow_percentile)
    shadows_mask = l < shadow_threshold

    mask = otsu_mask ^ shadows_mask

    return mask


image_path2 = './Objects_007_flash.png'  # e.g. https://notebooks.azure.com/clewolff/libraries/otsu/raw/golf2.jpg
image2 = cv2.imread(image_path2)
mask_otsu_shadows = compute_otsu_mask_shadows(image2)
show_mask(mask_otsu_shadows, image2, title='Otsu thresholding on the hue channel with shadow removal')
