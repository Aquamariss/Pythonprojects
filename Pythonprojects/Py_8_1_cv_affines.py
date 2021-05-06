import cv2
import numpy
import math

width = 500
height = 400
phi = math.pi/4.0

M_trans = numpy.float32([[1, 0, 0], [0, 1, 0], [50, 50, 1]]).T
#M_trans = numpy.float32([[1, 0, 50], [0, 1, 50], [0, 0, 1]])

M_rot = cv2.getRotationMatrix2D((width/2, height/2), phi/math.pi*180.0, 1.0)
M_shear = numpy.float32([[1, 0, 0], [0.25, 1, 0], [0, 0, 1]]).T

for i in range(1):
    image = cv2.imread(f"C:\SoftLearn\PythonExamples\mask{i+1}.jpg")
    imS = cv2.resize(image, (400, 300))
    cv2.imshow(f"Image {i+1} before affine changes", imS)
    cv2.waitKey(0)
    # apply transition
    result1 = cv2.warpPerspective(imS, M_trans, (width, height))

    cv2.imshow(f"Image {i + 1} after Transition", result1)
    cv2.waitKey(0)

    result2 = cv2.warpAffine(imS, M_rot, (width, height))
    cv2.imshow(f"Image {i + 1} after Rotation", result2)
    cv2.waitKey(0)


    result3 = cv2.warpPerspective(imS, M_shear, (width, height))
    cv2.imshow(f"Image {i + 1} after Shear", result3)
    cv2.waitKey(0)
