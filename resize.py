import os
from PIL import Image

# 文件输入路径
in_path = 'C:\\Users\\DELL\\Desktop\\smoke_detection\\原始尺寸烟雾数据集\\'

# 文件输出路径
out_path = 'C:\\Users\\DELL\\Desktop\\smoke_detection\\统一尺寸烟雾数据集\\'

# 获取所有文件名称
files = os.listdir(in_path)

# 处理图片
for i, file in enumerate(files):
    # 读取图片
    img = Image.open(in_path + file)

    # 图片尺寸转换
    img = img.resize((48, 48),Image.ANTIALIAS)

    # 图片输出
    img.save(out_path + file)