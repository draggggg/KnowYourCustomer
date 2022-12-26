try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
from pytesseract import Output
import cv2
import numpy as np
from matplotlib import pyplot as plt
from ArabicOcr import arabicocr
import json 


# Cropping ID photo
imagePath = r'aaa.jpg'
dirCascadeFiles = r'../opencv/haarcascades_cuda/'
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cascadefile = dirCascadeFiles + "haarcascade_frontalface_default.xml"
classCascade = cv2.CascadeClassifier(cascadefile)
faces = classCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print("Il y a {0} visage(s).".format(len(faces)))
# Coordonnées des rectangles des visages détectés (x, y, w, h)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
plt.imshow(image)



# Extractin the photo
f = faces[0]
plt.imshow(image[f[1]:f[1]+f[3], f[0]:f[0]+f[2]])

# extracting data from ID card

path_to_tesseract = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

image_path='C:\\Users\\anisg\Desktop\\hydatis\\aaa.jpg'
out_image='C:\\Users\\anisg\Desktop\\hydatis\\out.jpg'

pytesseract.tesseract_cmd = path_to_tesseract

img = Image.open(image_path)

results=arabicocr.arabic_ocr(image_path,out_image)
print(results)
words=[]
for i in range(len(results)):	
		word=results[i][1]
		words.append(word)
with open ('file.txt','w',encoding='utf-16')as myfile:
		myfile.write(str(words))
jsonString = json.dumps(words)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close()

# other solution to extract data from the ID with cutting the photo
image = cv2.imread(image_path)
x = 100
y = 65
w = 450
h = 87
plt.imshow(cv2.rectangle(image, (x, y), (w, h), (0, 255, 0), 2))

region_Nom = image[y:h, x:w]
plt.imshow(region_Nom)

NomCI = pytesseract.image_to_string(region_Nom)
print(NomCI)