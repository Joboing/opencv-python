#!/usr/bin/env python3
# -*- coding:utf-8 -*-
u'''
Created on 2020年5月15日
@author: Joboing
'''

import cv2
import numpy as np
import hnswlib
from matplotlib import pyplot as plt
import imutils

# 读取图片1
img = cv2.imread(
    'D:/data/image_retrieval/data/mater_videos/msdk/303/4774/5/303_4774_5_14_200/158172004370890673-00dd9366f6e49ad68ef86bfaba8228f8-1-0-1589432329282.jpg')
# 缩放0.2倍，不然图像显示太大了
# img = imutils.rotate(img, -90)
# 读取图片2
img1 = cv2.imread('D:/data/image_retrieval/data/mater_videos/msdk/303/4774/5/303.png')
#img1 = imutils.rotate(img1, 90)
# 把图片2缩放成图片1的大小，因为后面要把两张图片拼起来画对应特征点的连线
#img1 = cv2.resize(img1, (img.shape[1], img.shape[0]))
print(img.shape, img1.shape)
# 处理成灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
# 下面是提取sift特征
sift = cv2.xfeatures2d.SIFT_create(contrastThreshold=0.1)
# sift1 = cv2.xfeatures2d.SIFT_create(contrastThreshold=0.1)
# kp是特征点（包括坐标信息），ds相当于特征点的特征（128维）
kp, ds = sift.detectAndCompute(gray, None)
kp1, ds1 = sift.detectAndCompute(gray1, None)
# kp1 = sift1.detect(gray1,None)
cv2.drawKeypoints(image=img, outImage=img,
                  keypoints=kp,
                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                  color=(51, 163, 236))
cv2.drawKeypoints(image=img1, outImage=img1,
                  keypoints=kp1,
                  flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS,
                  color=(0, 0, 255))

# BFmatcher with default parms
bf = cv2.BFMatcher(cv2.NORM_L2)
matches = bf.knnMatch(ds, ds1, k=2)

goodMatch = []
for m, n in matches:
    print(m.distance, n.distance)
    if m.distance < 0.3 * n.distance:
        goodMatch.append(m)
print(len(goodMatch))
img3 = cv2.drawMatches(gray, kp, gray1, kp1, goodMatch[:20], None, flags=2)

plt.imshow(img3)
plt.show()
