from skimage import measure
import matplotlib.pyplot as plt
import numpy as np
import cv2
import PIL
from PIL import Image
import os

for filename in os.listdir('new_different_frames'):
    first_im_read=None
    if not filename.startswith('.'):
        for filenameception in os.listdir('new_different_frames/' + str(filename)):
            if filenameception.endswith('.jpg'):
                if not os.path.exists('new_CLAHEd_frames'):
                    os.makedirs('new_CLAHEd_frames')
                if not os.path.exists("new_CLAHEd_frames/" + str(filename)):
                    os.makedirs("new_CLAHEd_frames/" + str(filename))
                
                new_im = cv2.imread("new_different_frames/" + str(filename) + '/' + str(filenameception))

                lab = cv2.cvtColor(new_im, cv2.COLOR_BGR2LAB)
                lab_planes = cv2.split(lab)

                clahe = cv2.createCLAHE(clipLimit=5.0)
                lab_planes[0] = clahe.apply(lab_planes[0])
                
                lab = cv2.merge(lab_planes)

                final_img = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)

                cv2.imwrite("new_CLAHEd_frames/" + str(filename) + '/' + str(filenameception), final_img)
