# -*- coding:utf8 -*-

import cv2
import os

if __name__ == '__main__':
    save_path = "save_image_path"
    base_dir = "videos_path"
    count = 1
    video_list = os.listdir(base_dir)
    for video in video_list:
        video_path = os.path.join(base_dir, video)
        videoCapture = cv2.VideoCapture(video_path)
        i = 0
        j = 0
        while 1:
            success, frame = videoCapture.read()
            i += 1
            if not success:
                print('video is all read')
                break
            if (i % count == 0):
                j += 1
                save_name = video.split('.')[0] + '_' + 'f' + str(i) + '.jpg' #image name video_name_fi.jpg
                save_path1 = save_path + video.split('.')[0] + '/'
                if not os.path.exists(save_path1):
                    os.makedirs(save_path1)
                cv2.imwrite(save_path1 + save_name, frame)
                print('image of %s is saved' % (save_name))
