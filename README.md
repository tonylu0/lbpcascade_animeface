# lbpcascade_animeface

The face detector for anime/manga using OpenCV.

Original release since 2011 at [OpenCVによるアニメ顔検出ならlbpcascade_animeface.xml](http://ultraist.hatenablog.com/entry/20110718/1310965532) (in Japanese)

## Usage

Download and place the cascade file into your project directory.

    wget https://raw.githubusercontent.com/nagadomi/lbpcascade_animeface/master/lbpcascade_animeface.xml

### Python Example to Crop and Delete images that failed to detect faces
### Be sure to NOT use this on the original set of images
```python
import cv2
import sys
import os.path

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
    for (x, y, w, h) in faces:
        crop_img = image[y:y+h, x:x+w]
        cv2.imwrite(filename, crop_img)
        flag = 1
    
    if (flag == 0) :
        try: 
            os.remove(filename)
        except: pass

```
Usage to crop folder
```python
import cv2
import sys
import os.path
directory = 'Hibiki_crop'
for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    detect(file)
 ```  
![result](https://imgur.com/vURNvkj)

## Note
I am providing similar project at https://github.com/nagadomi/animeface-2009. animeface-2009 is my original work that was made before libcascade_animeface. The detection accuracy is higher than this project. However, installation of that is a bit complicated. Also I am providing a face cropping script using animeface-2009.
