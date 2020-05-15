import cv2
from math import *
import numpy as np
import os


def rotate(img, save_path):
    img = cv2.imread(img)
    # img = Image.open(pic)
    img = np.array(img)
    height, width = img.shape[:2]

    degree = -90
    # 旋转后的尺寸
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
    print(height, width)
    print(heightNew, widthNew)
    # 获得仿射变化矩阵（中间点的位置，旋转角度（-90：逆时针旋转90度），1（等比例缩放））
    #opencv采用的方式：[[a,-b,(1-a)*centerx-b*centery],[-b,a,b*centery-(1-a)*centerx]]
    matRotation = cv2.getRotationMatrix2D((width / 2, height / 2), degree,1)
    print(matRotation)
    # matRotation[0, 2] += (widthNew - width) / 2  # 重点在这步，目前不懂为什么加这步
    # matRotation[1, 2] += (heightNew - height) / 2  # 重点在这步
    # 图片上的一个点(matRotation[0][0] * x + matRotation[0][1] * y + matRotation[0][2], matRotation[1][0] * x + matRotation[1][1] * y + matRotation[1][2] )
    imgRotation = cv2.warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(255, 255, 255))  # 进行仿射变化
    
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    cv2.imwrite(save_path+"imgname", imgRotation)

file_dir = "image_path"
save_path = "save_rotated_path"
rotate(file_dir, save_path)
