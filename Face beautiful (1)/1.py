import cv2 as cv


image = cv.imread('(1).png')
targer = cv.bilateralFilter(image,13,40,70)#13 40 70
cv.imshow("src",image)
cv.imshow("beauty",targer)
cv.waitKey(0)
