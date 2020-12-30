import os
from PIL import Image

# jpg 转 png
def jpg2png(jpg_path):
    img = Image.open(jpg_path)
    img.save(jpg_path.strip('.jpg') + '.png')

# 文件路径
path = 'C:\\Users\\DELL\\Desktop\\smoke_detection\\非烟雾\\'

# 获取所有文件名称
files = os.listdir(path)

# 处理图片
for i, file in enumerate(files):
    # jpg 转为 png
    # if file.endswith('.jpg'):
        # 修改文件后缀
        # jpg2png(path + file)

        # 删除图片
        # os.remove(path + file)

    # 新文件名称
    NewName = os.path.join(path, str(i + 603) + '.png')

    # 旧文件名称
    OldName = os.path.join(path, file)

    # 名称修改
    os.rename(OldName, NewName)