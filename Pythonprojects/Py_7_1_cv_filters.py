import cv2
import numpy
kernel_thr = numpy.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
kernel_sharp = numpy.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

threshold1 = 1
threshold2 = 300

for i in range(3):
    image = cv2.imread(f"C:\SoftLearn\PythonExamples\mask{i+1}.jpg")
    imS = cv2.resize(image, (400, 300))
    cv2.imshow(f"Image {i+1} before filter", imS)
    cv2.waitKey(0)
    # apply filter edge detection
    result2 = cv2.filter2D(imS, -1, kernel_sharp)
    cv2.imshow(f"Image {i + 1} after SharpenPy_7_1_cv_filters.py filter", result2)
    cv2.waitKey(0)

    result1 = cv2.filter2D(imS, -1, kernel_thr)
    cv2.imshow(f"Image {i + 1} after Edge 2d filter", result1)
    cv2.waitKey(0)


    result3 = cv2.Canny(imS, threshold1, threshold2)
    cv2.imshow(f"Image {i + 1} after Canny filter", result3)
    cv2.waitKey(0)
