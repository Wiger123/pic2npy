import numpy as np
import os
import cv2

# 图片输入地址
in_path = 'C:\\Users\\DELL\\Desktop\\smoke_detection\\smoke_data_same_shape\\'

# npy 输出地址
out_path = 'C:\\Users\\DELL\\Desktop\\smoke_detection\\smoke_data_output_file\\'

# 输出数组
res = []

# 获取所有文件名称
files = os.listdir(in_path)

# 处理图片
for i, file in enumerate(files):
    # 读取图片
    img = cv2.imread(in_path + file)

    # 压缩 255
    img = img / 255.0

    # 添加到列表
    res.append(img)

# 转换为数组
res = np.array(res)

# 显示尺寸
print(res.shape)

# 数组存为 npy
np.save(out_path + "smoke_data.npy", res)