import cv2
import numpy

image = cv2.imread('C:\SoftLearn\PythonExamples\image.jpg')
imS = cv2.resize(image, (400, 480))
cv2.imshow('Image before filter', imS)
cv2.waitKey(0)
# apply filter edge detection
kernel = numpy.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
result = cv2.filter2D(imS, -1, kernel)

cv2.imshow('Image after filter', result)
cv2.waitKey(0)
