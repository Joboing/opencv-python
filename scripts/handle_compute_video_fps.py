# -*- coding:utf8 -*-
import cv2

file_path = "video_path"
vc = cv2.VideoCapture(file_path)  # 读入视频文件
fps = vc.get(cv2.CAP_PROP_FPS)
print(fps)
