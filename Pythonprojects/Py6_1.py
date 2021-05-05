import cv2
image = cv2.imread('C:\SoftLearn\PythonExamples\image.jpg')
imS = cv2.resize(image, (400, 480))
imS_bgr = cv2.cvtColor(imS,cv2.COLOR_RGB2BGR)
cv2.imshow('My second image', imS_bgr)
cv2.waitKey(0)
print(image.shape)
print(imS.shape)
cv2.imwrite('C:\SoftLearn\PythonExamples\image_bgr.jpg',imS_bgr)

height, weight, n_channels = image.shape

channels = cv2.split(imS)
print("BGR model - channels")
l = len(channels) #0-B,1-G,2-R
for i in range(l):
    print(i)
    cv2.imshow(' channel of image', channels[i])
    cv2.waitKey(0)

imH = cv2.cvtColor(imS,cv2.COLOR_RGB2HSV)
channels = cv2.split(imH)
print("HSV model - channels")
l = len(channels) #0-H,1-S,2-V
for i in range(l):
    print(i)
    cv2.imshow(' channel of image', channels[i])
    cv2.waitKey(0)
