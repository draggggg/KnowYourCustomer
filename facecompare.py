def compare_faces(path_to_img1, path_to_img2):
  from deepface import DeepFace
  import cv2 as cv
  img1 = cv.imread(path_to_img1)
  img2 = cv.imread(path_to_img2)


  result = DeepFace.verify(img1,img2)
  return result["verified"]
