import cv2
import os

folder='/home/theone/anaconda3/positive_images'

for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename), cv2.IMREAD_GRAYSCALE)
    img2=cv2.resize(img,(50,50))
    cv2.imwrite('/home/theone/anaconda3/positive_images/'+filename,img2)

folder='/home/theone/anaconda3/negative_images'

for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename), cv2.IMREAD_GRAYSCALE)
    img2=cv2.resize(img,(50,50))
    cv2.imwrite('/home/theone/anaconda3/negative_images/'+filename,img2)
