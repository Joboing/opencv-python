# 主要是需要moviepy这个库
from moviepy.editor import *
import os
from natsort import natsorted
'''
notes 
合成视频的尺寸必须一样，否则后面的视频会出现花屏
'''
# 定义一个数组
L = []

# 访问 video 文件夹 (假设视频都放在这里面)
video_dir = "./merge_video"
for root, dirs, files in os.walk(video_dir):
    # 按文件名排序
    files = natsorted(files)
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == '.mp4':
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            # 载入视频
            video = VideoFileClip(filePath)
            # 添加到数组
            L.append(video)

# 拼接视频
final_clip = concatenate_videoclips(L)

# 生成目标视频文件
final_clip.to_videofile("./t/merge_video/target.mp4", fps=25,
                        remove_temp=False)
