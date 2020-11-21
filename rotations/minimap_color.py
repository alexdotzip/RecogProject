#Finds the minimap for Moscow Hardpoint
import cv2
import numpy as np
import matplotlib.pyplot as pylab

img = cv2.imread('../Work/data/frame250.jpg')
dimensions = img.shape
total_number_of_elements = img.size
image_dtype = img.dtype

minimap = img[750:1080, 45:600]
cv2.imshow("Minimap", minimap)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)