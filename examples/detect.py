import cv2
import sys
import os.path
import os


def detect(filename, cascade_file = "lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    flag = 0
    count = 1
    for (x, y, w, h) in faces:
        crop_img = image[y:y+h, x:x+w]
        if len(faces) > 1:
            base = os.path.splitext(filename)[0]
            extension = os.path.splitext(filename)[1]
            newfilename = base + str(count) + extension
            cv2.imwrite(newfilename, crop_img)
        else:
            cv2.imwrite(filename, crop_img)
        flag = 1
        count += 1
        
    if len(faces) > 1:
        try: 
            os.remove(filename)
        except: pass
    
    if (flag == 0) :
        try: 
            os.remove(filename)
        except: pass
 
#     for (x, y, w, h) in faces:
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

#     cv2.imshow("AnimeFaceDetect", image)
#     cv2.waitKey(0)
#     cv2.imwrite("out.png", image)

def cropFolder(foldername):
    directory = foldername
    for filename in os.listdir(directory):
        file = os.path.join(directory, filename)
        detect(file)
