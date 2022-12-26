from deepface import DeepFace
import cv2 as cv
import matplotlib.pyplot as plt

img1 = cv.imread(r'C:\Users\lenovo\Desktop\OCR\passeport.jpg')


img2 = cv.imread(r'C:\Users\lenovo\Desktop\OCR\Pdp.jpg')


result = DeepFace.verify(img1,img2)
print(result["verified"])